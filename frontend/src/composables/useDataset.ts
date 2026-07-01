import { computed } from 'vue'
import { useDataStore } from '@/stores/dataStore'

export function useDataset() {
  const dataStore = useDataStore()
  return computed(() => dataStore.data?.dataset ?? [])
}
