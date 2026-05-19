<template>
  <div class="card">
    <h2 class="text-lg font-bold mb-2">Full Ranking</h2>
    <DataTable
      :value="resultTable"
      stripedRows
      class="border border-surface-200 dark:border-surface-700 rounded-lg overflow-hidden"
    >
      <Column field="alternative" header="Alternative" class="font-bold text-primary"></Column>
      <Column
        v-for="method in methodNames"
        :key="method"
        :field="method"
        :header="method.toUpperCase()"
      ></Column>
    </DataTable>
  </div>
</template>

<script setup lang="ts">
import { useDataStore } from '@/stores/dataStore'
import { useResultsStore } from '@/stores/resultsStore'

import DataTable from 'primevue/datatable'
import Column from 'primevue/column'

import { computed } from 'vue'

const dataStore = useDataStore()
const resultsStore = useResultsStore()

const dataSet = computed(() => dataStore.data?.dataset ?? [])
const rankings = computed(() => resultsStore.results?.rankings ?? {})
const methodNames = computed(() => Object.keys(rankings.value))

const resultTable = computed(() => {
  return dataSet.value.map((row, i) => {
    const individualRank = Object.fromEntries(
      Object.entries(rankings.value).map(([method, methodRank]) => [method, methodRank[i]]),
    )
    return {
      alternative: row.alternative,
      ...individualRank,
    }
  })
})
</script>
