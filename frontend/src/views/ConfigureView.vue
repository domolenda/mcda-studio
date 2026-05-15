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

async function runAnalysis() {
  if (dataStore.data === null) return
  if (configStore.weights === null) return
  if (configStore.selectedMethodCount === null || configStore.selectedMethodCount === 0) return
  if (configStore.dataMatrix === null) return
  if (configStore.methodsConfig.length === 0) return

  const request: BaseRankingRequest = {
    matrix: configStore.dataMatrix,
    types: dataStore.data.criteria.map((c) => c.type),
    weights: configStore.weights,
  }

  if (configStore.selectedMethodCount === 1) {
    const method = configStore.methodsConfig[0]
    let result: SingleRankingResponse | null = null

    switch (method.name) {
      case 'topsis':
        const topsisRequest: TOPSISRequest = {
          ...request,
          normalization_method: method.params.find((param) => param.name === 'normalization_method')
            ?.value,
        }
        result = await rankTopsis(topsisRequest)
        break
      case 'waspas':
        const waspasRequest: WASPASRequest = {
          ...request,
          normalization_method: method.params.find((param) => param.name === 'normalization_method')
            ?.value,
          lambda_: method.params.find((param) => param.name === 'lambda_')?.value,
        }
        result = await rankWaspas(waspasRequest)
        break
      case 'vikor':
        const vikorRequest: VIKORRequest = {
          ...request,
          v: method.params.find((param) => param.name === 'v')?.value,
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
  } else if (configStore.selectedMethodCount > 1) {
    const comparisonRequest: ComparisonRequest = {
      ...request,
      methods_config: configStore.methodsConfig,
    }
    const resultComparison: MultipleResultData = await getComparisonResults(comparisonRequest)
    resultsStore.setResults(resultComparison)
    router.push({ name: 'results' })
  }
}
</script>
