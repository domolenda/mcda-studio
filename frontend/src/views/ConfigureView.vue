<template>
  <div v-if="dataStore.data">
    <WeightsConfig />
    <MethodsConfig />
    <div class="flex justify-center mt-4">
      <Button
        label="Run Analysis"
        @click="runAnalysis"
        class="bg-primary border-primary hover:brightness-110"
      />
    </div>
  </div>
  <div v-else class="text-center p-8 text-surface-500">
    No data available. Please upload a dataset first.
  </div>
</template>

<script setup lang="ts">
import WeightsConfig from '@/components/configure/WeightsConfig.vue'
import MethodsConfig from '@/components/configure/MethodsConfig.vue'
import Button from 'primevue/button'

import { useRouter } from 'vue-router'
import { useToast } from 'primevue/usetoast'

import { useDataStore } from '@/stores/dataStore'
import { useConfigStore } from '@/stores/configStore'
import { useResultsStore } from '@/stores/resultsStore'

import { rankTopsis, rankWaspas, rankVikor, getComparisonResults } from '@/services/api'
import type {
  BaseRankingRequest,
  TOPSISRequest,
  WASPASRequest,
  VIKORRequest,
  ComparisonRequest,
  SingleRankingResponse,
  MultipleResultData,
} from '@/types'

const dataStore = useDataStore()
const configStore = useConfigStore()
const resultsStore = useResultsStore()
const router = useRouter()
const toast = useToast()

function validateConfig(): boolean {
  if (dataStore.data === null) return false
  if (configStore.weights === null) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'Please set weights first.',
      life: 3000,
    })
    return false
  }

  const weightsSum = configStore.weights.reduce((acc, val) => acc + (val || 0), 0)
  if (Math.abs(weightsSum - 1) > 1e-9) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'Weights must sum to 1.',
      life: 3000,
    })
    return false
  }

  if (configStore.selectedMethodCount === null || configStore.selectedMethodCount === 0) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'Please select number of methods for analysis.',
      life: 3000,
    })
    return false
  }
  if (configStore.dataMatrix === null) return false
  if (configStore.methodsConfig.length === 0) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'Please configure methods for analysis.',
      life: 3000,
    })
    return false
  }
  const methodNames = configStore.methodsConfig.map((m) => m.name)
  const uniqueNames = new Set(methodNames)
  if (methodNames.length !== uniqueNames.size) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'Selected MCDA methods must be unique.',
      life: 3000,
    })
    return false
  }

  return true
}

async function runAnalysis() {
  if (!validateConfig()) return

  const request: BaseRankingRequest = {
    matrix: configStore.dataMatrix!,
    types: dataStore.data!.criteria.map((c) => c.type),
    weights: configStore.weights!,
  }

  try {
    if (configStore.selectedMethodCount === 1) {
      const method = configStore.methodsConfig[0]
      if (!method) return
      let result: SingleRankingResponse | null = null

      switch (method.name) {
        case 'topsis':
          const topsisRequest: TOPSISRequest = {
            ...request,
            normalization_method: method.params.find(
              (param) => param.name === 'normalization_method',
            )?.value as string | undefined,
          }
          result = await rankTopsis(topsisRequest)
          break
        case 'waspas':
          const waspasRequest: WASPASRequest = {
            ...request,
            normalization_method: method.params.find(
              (param) => param.name === 'normalization_method',
            )?.value as string | undefined,
            lambda_: method.params.find((param) => param.name === 'lambda_')?.value as
              | number
              | undefined,
          }
          result = await rankWaspas(waspasRequest)
          break
        case 'vikor':
          const vikorRequest: VIKORRequest = {
            ...request,
            v: method.params.find((param) => param.name === 'v')?.value as number | undefined,
          }
          result = await rankVikor(vikorRequest)
          break
      }
      if (result) {
        const mappedResult: MultipleResultData = {
          rankings: { [method.name]: result.ranking },
          correlations: [],
        }
        resultsStore.setResults(mappedResult)
        router.push({ name: 'results' })
      }
    } else if (configStore.selectedMethodCount! > 1) {
      const comparisonRequest: ComparisonRequest = {
        ...request,
        methods_config: configStore.methodsConfig,
      }
      const resultComparison: MultipleResultData = await getComparisonResults(comparisonRequest)
      resultsStore.setResults(resultComparison)
      router.push({ name: 'results' })
    }
  } catch {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail:
        'There was an error processing your request. Please try again later or check your data with configuration.',
      life: 3000,
    })
  }
}
</script>
