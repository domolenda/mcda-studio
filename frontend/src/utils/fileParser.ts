import Papa from 'papaparse'
import * as XLSX from 'xlsx'
import type { Criterion, Dataset, ProcessedProjectData } from '@/types'

export async function parseCSV(file: File): Promise<Papa.ParseResult<unknown>> {
  return new Promise((resolve, reject) => {
    Papa.parse(file, {
      header: true,
      skipEmptyLines: true,
      dynamicTyping: true,
      complete: (result) => {
        resolve(result)
      },
      error: (error) => {
        reject(error)
      },
    })
  })
}

export async function parseExcel(file: File): Promise<(string | number)[][]> {
  const buffer = await file.arrayBuffer()
  const workbook = XLSX.read(buffer)
  const sheetName: string | undefined = workbook.SheetNames[0]
  if (!sheetName) {
    throw new Error('No sheets found in the file.')
  }
  const sheet = workbook.Sheets[sheetName]
  if (!sheet) {
    throw new Error('Could not read sheet from the file.')
  }
  const data = XLSX.utils.sheet_to_json(sheet, { header: 1 })
  return data as (string | number)[][]
}

export function processCSVResult(result: Papa.ParseResult<unknown>): ProcessedProjectData {
  const fields = result.meta.fields ?? []
  const alternativeKey: string | undefined = fields[0]
  const criteriaKeys: string[] = fields.slice(1)

  if (!alternativeKey) {
    throw new Error('No alternative key found in CSV.')
  }

  const dataset: Dataset = (result.data as Record<string, unknown>[]).map((row) => ({
    alternative: row[alternativeKey] as string,
    values: criteriaKeys.map((c) => row[c] as number),
  }))

  const criteria: Criterion[] = criteriaKeys.map((c) => ({ name: c, type: 1 as const }))
  const processedProjectData: ProcessedProjectData = { dataset, criteria, alternativeKey }

  return processedProjectData
}

export function processExcelResult(data: (string | number)[][]): ProcessedProjectData {
  const fields = data[0] as string[]
  const criteriaKeys: string[] = fields.slice(1)
  const alternativeKey = fields[0]

  if (!alternativeKey) {
    throw new Error('No alternative key found in Excel.')
  }

  const dataset: Dataset = data.slice(1).map((row) => ({
    alternative: row[0] as string,
    values: row.slice(1).map((v) => v as number),
  }))

  const criteria: Criterion[] = criteriaKeys.map((c) => ({ name: c, type: 1 }))
  const processedProjectData: ProcessedProjectData = { dataset, criteria, alternativeKey }

  return processedProjectData
}
