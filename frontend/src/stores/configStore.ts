import { defineStore } from 'pinia'
import { ref } from 'vue'
import { type ConfigData } from '@/types'

export const useConfigStore = defineStore('config', () => {
  const methodList = ref<string[] | null>(null)
  const weights = ref<number[] | null>(null)
  const methodsConfig = ref<ConfigData[] | null>(null)
  const dataMatrix = ref<number[][] | null>(null)
  const selectedMethodCount = ref<number | null>(null)

  function setMethodList(newMethodList: string[]) {
    methodList.value = newMethodList
  }

  function clearMethodList() {
    methodList.value = null
  }

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
    methodsConfig.value = null
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
    clearMethodList()
    clearWeights()
    clearMethodsConfig()
    clearDataMatrix()
    clearSelectedMethodCount()
  }

  return {
    methodList,
    setMethodList,
    clearMethodList,
    weights,
    setWeights,
    clearWeights,
    methodsConfig,
    setMethodsConfig,
    clearMethodsConfig,
    dataMatrix,
    setDataMatrix,
    clearDataMatrix,
    clearConfig,
    selectedMethodCount,
    setSelectedMethodCount,
    clearSelectedMethodCount,
  }
})
