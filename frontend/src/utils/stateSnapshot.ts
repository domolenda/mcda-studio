import { useDataStore } from '@/stores/dataStore'
import { useConfigStore } from '@/stores/configStore'
import { useResultsStore } from '@/stores/resultsStore'

const APP_VERSION = import.meta.env.VITE_APP_VERSION

export function saveStateSnapshot() {
  const dataStore = useDataStore()
  const configStore = useConfigStore()
  const resultsStore = useResultsStore()

  const snapshot = {
    version: APP_VERSION,
    data: dataStore.data,
    config: {
      weights: configStore.weights,
      methodsConfig: configStore.methodsConfig,
      dataMatrix: configStore.dataMatrix,
      selectedMethodCount: configStore.selectedMethodCount,
    },
    results: resultsStore.results,
  }

  const blob = new Blob([JSON.stringify(snapshot)], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const filename = `mcda-studio-state-${APP_VERSION}.json`
  const link = document.createElement('a')
  link.href = url
  link.download = filename
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
  URL.revokeObjectURL(url)
}

export function loadStateSnapshot(file: File) {
  const dataStore = useDataStore()
  const configStore = useConfigStore()
  const resultsStore = useResultsStore()

  const reader = new FileReader()
  reader.onload = (e) => {
    const snapshot = JSON.parse(e.target?.result as string)
    dataStore.setData(snapshot.data)

    configStore.setWeights(snapshot.config.weights)
    configStore.setMethodsConfig(snapshot.config.methodsConfig)
    configStore.setDataMatrix(snapshot.config.dataMatrix)
    configStore.setSelectedMethodCount(snapshot.config.selectedMethodCount)

    resultsStore.setResults(snapshot.results)
  }
  reader.readAsText(file)
}

export function resetStoreState() {
  const dataStore = useDataStore()
  const configStore = useConfigStore()
  const resultsStore = useResultsStore()

  dataStore.clearData()
  configStore.clearConfig()
  resultsStore.clearResults()
}
