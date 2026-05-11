import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { ProcessedProjectData, CriterionType } from '@/types'

export const useDataStore = defineStore('data', () => {
  const data = ref<ProcessedProjectData | null>(null)

  function setData(newData: ProcessedProjectData) {
    data.value = newData
  }

  function clearData() {
    data.value = null
  }

  function setCriterionType(index: number, type: CriterionType) {
    if (data.value && data.value.criteria[index]) {
      data.value.criteria[index].type = type
    }
  }

  return { data, setData, clearData, setCriterionType }
})
