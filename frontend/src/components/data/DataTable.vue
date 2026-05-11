<template>
  <div class="card p-6">
    <DataTable
      v-if="dataStore.data"
      :value="dataSet"
      stripedRows
      class="border border-surface-200 dark:border-surface-700 rounded-lg overflow-hidden"
    >
      <Column field="alternative" :header="headers[0]" class="font-bold text-primary"></Column>

      <Column v-for="(header, index) in headers.slice(1)" :key="header" :header="header">
        <template #body="slotProps">
          {{ slotProps.data.values[index] }}
        </template>
      </Column>
    </DataTable>

    <div v-else class="text-center p-8 text-surface-500">No data available</div>
  </div>
</template>

<script setup lang="ts">
import { useDataStore } from '@/stores/dataStore'
import { computed } from 'vue'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'

const dataStore = useDataStore()

const dataSet = computed(() => dataStore.data?.dataset ?? [])

const headers = computed(() => {
  const data = dataStore.data
  if (!data || !data.criteria) return []

  const altKey = data.alternativeKey || 'Alternative'

  const criterionNames = data.criteria.map((c) => c.name)

  return [altKey, ...criterionNames]
})
</script>
