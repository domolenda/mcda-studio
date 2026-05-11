import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { ProcessedProjectData } from '@/types'

export const useDataStore = defineStore('data', () => {
  const data = ref<ProcessedProjectData | null>(null)

  function setData(newData: ProcessedProjectData) {
    data.value = newData
  }

  function clearData() {
    data.value = null
  }

  return { data, setData, clearData }
})
