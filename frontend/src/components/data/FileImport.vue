<template>
  <div class="card flex justify-center p-6">
    <FileUpload
      mode="basic"
      accept=".csv, .txt, .xlsx, .xls"
      @select="onFileSelect"
      chooseLabel="Upload Data File"
      class="bg-primary border-primary hover:brightness-110"
    />
  </div>
</template>

<script setup lang="ts">
import FileUpload, { type FileUploadSelectEvent } from 'primevue/fileupload'
import { parseCSV, parseExcel, processCSVResult, processExcelResult } from '@/utils/fileParser'
import { useDataStore } from '@/stores/dataStore'
import { useConfigStore } from '@/stores/configStore'
import { useResultsStore } from '@/stores/resultsStore'
import { useToast } from 'primevue/usetoast'

const dataStore = useDataStore()
const configStore = useConfigStore()
const resultsStore = useResultsStore()
const toast = useToast()

const CSV_EXTENSIONS = ['.csv', '.txt']
const EXCEL_EXTENSIONS = ['.xlsx', '.xls']

const onFileSelect = (event: FileUploadSelectEvent) => {
  const file = event.files[0]
  if (file) {
    processFile(file)
  }
}

async function processFile(file: File) {
  const extension = file.name.slice(file.name.lastIndexOf('.')).toLowerCase()

  try {
    let result
    if (CSV_EXTENSIONS.includes(extension)) {
      result = await parseCSV(file)
      result = processCSVResult(result)
    } else if (EXCEL_EXTENSIONS.includes(extension)) {
      result = await parseExcel(file)
      result = processExcelResult(result)
    }
    if (!result) {
      toast.add({
        severity: 'error',
        summary: 'Error',
        detail: 'Unsupported file format. Please use CSV, TXT, XLSX or XLS.',
        life: 3000,
      })
      return
    }
    dataStore.setData(result)
    if (resultsStore.results) {
      resultsStore.clearResults()
    }
    if (configStore.methodList || configStore.weights || configStore.methodsConfig) {
      configStore.clearConfig()
    }
    const dataMatrix = result.dataset.map((row) => row.values)
    configStore.setDataMatrix(dataMatrix)
  } catch {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'Failed to parse file. Check if the file structure is correct.',
      life: 3000,
    })
  }
}
</script>
