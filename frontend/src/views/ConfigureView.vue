<template>
  <div v-if="dataStore.data">
    <WeightsConfig />
    <MethodsConfig />
  </div>
  <div v-else class="text-center p-8 text-surface-500">
    No data available. Please upload a dataset first.
  </div>
</template>

<script setup lang="ts">
import WeightsConfig from '@/components/configure/WeightsConfig.vue'
import MethodsConfig from '@/components/configure/MethodsConfig.vue'

import { useDataStore } from '@/stores/dataStore'

const dataStore = useDataStore()
</script>
