import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { MultipleResultData } from '@/types'

export const useResultsStore = defineStore('results', () => {
  const results = ref<MultipleResultData | null>(null)

  function setResults(newResults: MultipleResultData) {
    results.value = newResults
  }

  function clearResults() {
    results.value = null
  }

  return { results, setResults, clearResults }
})
