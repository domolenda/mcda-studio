<template>
  <div v-if="dataStore.data && resultsStore.results" class="p-4 mx-auto">
    <div
      class="border border-surface-200 dark:border-surface-700 rounded-lg p-4 bg-white dark:bg-surface-900"
    >
      <RankingTable />
    </div>
    <div v-if="resultsStore.results.correlations.length > 0" class="mt-4 p-4">
      <div class="flex flex-wrap gap-4 justify-center">
        <CorrelationScatter />
      </div>
    </div>
  </div>
  <div v-else class="text-center p-8 text-surface-500">
    No data available. Please run analysis first.
  </div>
</template>

<script setup lang="ts">
import { useDataStore } from '@/stores/dataStore'
import { useResultsStore } from '@/stores/resultsStore'

import RankingTable from '@/components/results/RankingTable.vue'
import CorrelationScatter from '@/components/results/CorrelationScatter.vue'

const dataStore = useDataStore()
const resultsStore = useResultsStore()
</script>
