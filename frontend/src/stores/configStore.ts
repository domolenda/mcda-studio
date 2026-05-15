import { defineStore } from 'pinia'
import { ref } from 'vue'
import { type ConfigData } from '@/types'

export const useConfigStore = defineStore('config', () => {
  const weights = ref<number[] | null>(null)
  const methodsConfig = ref<ConfigData[]>([])
  const dataMatrix = ref<number[][] | null>(null)
  const selectedMethodCount = ref<number | null>(null)

  function setWeights(newWeights: number[]) {
    weights.value = newWeights
  }

  function clearWeights() {
    weights.value = null
  }

  function setMethodsConfig(newMethodsConfig: ConfigData[]) {
    methodsConfig.value = newMethodsConfig
  }

  function clearMethodsConfig() {
    methodsConfig.value = []
  }

  function addMethodConfig(id: number, config: ConfigData) {
    methodsConfig.value[id] = config
  }

  function setDataMatrix(newDataMatrix: number[][]) {
    dataMatrix.value = newDataMatrix
  }

  function clearDataMatrix() {
    dataMatrix.value = null
  }

  function setSelectedMethodCount(newCount: number) {
    selectedMethodCount.value = newCount
  }

  function clearSelectedMethodCount() {
    selectedMethodCount.value = null
  }

  function clearConfig() {
    clearWeights()
    clearMethodsConfig()
    clearDataMatrix()
    clearSelectedMethodCount()
  }

  return {
    weights,
    setWeights,
    clearWeights,
    methodsConfig,
    setMethodsConfig,
    clearMethodsConfig,
    addMethodConfig,
    dataMatrix,
    setDataMatrix,
    clearDataMatrix,
    clearConfig,
    selectedMethodCount,
    setSelectedMethodCount,
    clearSelectedMethodCount,
  }
})
