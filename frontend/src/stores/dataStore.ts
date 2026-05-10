import { defineStore } from 'pinia'
import { ref } from 'vue'
import { type ProjectData } from '@/types'

export const useDataStore = defineStore('data', () => {
  const data = ref<ProjectData | null>(null)

  function setData(newData: ProjectData) {
    data.value = newData
  }

  function clearData() {
    data.value = null
  }

  return { data, setData, clearData }
})
