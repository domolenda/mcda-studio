<template>
  <div v-if="dataStore.data && resultsStore.results"></div>
  <div v-else class="text-center p-8 text-surface-500">
    No data available. Please run analysis first.
  </div>
</template>

<script setup lang="ts">
import { useDataStore } from '@/stores/dataStore'
import { useResultsStore } from '@/stores/resultsStore'

const dataStore = useDataStore()
const resultsStore = useResultsStore()
</script>
