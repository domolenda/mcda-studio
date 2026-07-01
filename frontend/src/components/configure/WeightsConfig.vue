<template>
  <div class="card p-6" v-if="tableData">
    <DataTable
      :value="tableData"
      :showHeader="false"
      stripedRows
      :pt="{
        thead: { class: 'hidden' },
      }"
      tableStyle="min-width: 100%"
      class="border border-surface-200 dark:border-surface-700 rounded-lg overflow-hidden"
    >
      <Column field="type" class="font-bold"></Column>
      <Column v-for="(_, idx) in criterionNames" :key="idx" :field="idx.toString()">
        <template #body="slotProps">
          <div v-if="slotProps.data.type === 'Weights'">
            <InputNumber
              v-model="weights[idx]"
              :min="0"
              :max="1"
              :minFractionDigits="1"
              :maxFractionDigits="20"
              :allowEmpty="false"
              mode="decimal"
              inputClass="w-full text-center py-1 px-2 border rounded-md dark:bg-surface-900"
            />
          </div>
          <div v-else>{{ slotProps.data[idx.toString()] }}</div>
        </template>
      </Column>
    </DataTable>
    <div class="flex justify-between items-center mt-4">
      <div class="flex gap-2 font-bold">
        <Button
          label="Equal Weights"
          @click="handleObjectiveWeights('equal')"
          class="bg-primary border-primary hover:brightness-110"
        />
        <Button
          label="Entropy Weights"
          @click="handleObjectiveWeights('entropy')"
          class="bg-primary border-primary hover:brightness-110"
        />
      </div>
      <div
        class="border border-surface-200 dark:border-surface-700 rounded-lg p-2 font-bold bg-white dark:bg-surface-900"
      >
        <span :class="weightsSum !== 1 ? 'text-red-600' : 'text-green-500'"
          >Sum: {{ weightsSum }}</span
        >
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useDataStore } from '@/stores/dataStore'
import { useConfigStore } from '@/stores/configStore'
import { computed, watch } from 'vue'
import type { TableRow, WeightsRequest } from '@/types'

import { showToast } from '@/utils/toastUtils'

import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import InputNumber from 'primevue/inputnumber'
import Button from 'primevue/button'

import { getEntropyWeights, getEqualWeights } from '@/services/api'

const dataStore = useDataStore()
const configStore = useConfigStore()

const criteria = computed(() => dataStore.data?.criteria ?? [])
const criterionNames = computed(() => criteria.value.map((c) => c.name))

const weights = computed<number[]>({
  get() {
    return configStore.weights ?? createEmptyWeights()
  },
  set(value: number[]) {
    configStore.setWeights(value)
  },
})

const tableData = computed(() => {
  const namesRow: TableRow = { type: 'Criteria' }
  const weightsRow: TableRow = { type: 'Weights' }

  criterionNames.value.forEach((name, i) => {
    const key = i.toString()
    namesRow[key] = name
    weightsRow[key] = 0
  })

  return [namesRow, weightsRow]
})

const weightsSum = computed(() => {
  const sum = weights.value.reduce((acc, val) => acc + (val || 0), 0)
  return parseFloat(sum.toFixed(10))
})

async function handleObjectiveWeights(type: 'equal' | 'entropy') {
  try {
    if (!configStore.dataMatrix || configStore.dataMatrix.length === 0) {
      throw new Error('Data matrix is empty')
    }

    const request: WeightsRequest = { matrix: configStore.dataMatrix }
    const response =
      type === 'equal' ? await getEqualWeights(request) : await getEntropyWeights(request)

    if (!response.weights || response.weights.length === 0) {
      throw new Error('No weights returned')
    }
    weights.value = response.weights
  } catch (error) {
    const detail = error instanceof Error ? error.message : 'Failed to generate weights.'
    showToast(detail)
    return
  }
}

function createEmptyWeights() {
  return Array.from({ length: criterionNames.value.length }, () => 0)
}

watch(
  criterionNames,
  (newValue) => {
    const savedWeights = configStore.weights
    if (savedWeights && savedWeights.length === newValue.length) {
      weights.value = [...savedWeights]
    } else {
      weights.value = createEmptyWeights()
    }
  },
  { immediate: true },
)
</script>
