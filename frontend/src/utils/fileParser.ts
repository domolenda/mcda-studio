import Papa from 'papaparse'
import * as XLSX from 'xlsx'
import type { Criterion, Dataset, ProcessedProjectData } from '@/types'

export async function parseCSV(file: File): Promise<Papa.ParseResult<unknown>> {
  return new Promise((resolve, reject) => {
    Papa.parse(file, {
      header: true,
      skipEmptyLines: true,
      dynamicTyping: true,
      complete: resolve,
      error: reject,
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

function isString(value: unknown): value is string {
  return typeof value === 'string'
}

function isNumber(value: unknown): value is number {
  return typeof value === 'number'
}

function buildProjectData(
  dataset: { alternative: string; values: number[] }[],
  criteriaKeys: string[],
  alternativeKey: string,
): ProcessedProjectData {
  const criteria: Criterion[] = criteriaKeys.map((c) => ({ name: c, type: 1 }))
  return { dataset, criteria, alternativeKey }
}

export function processCSVResult(result: Papa.ParseResult<unknown>): ProcessedProjectData {
  const fields = result.meta.fields ?? []
  const alternativeKey = fields[0]

  if (!alternativeKey) {
    throw new Error('No alternative key found in CSV.')
  }

  const criteriaKeys = fields.slice(1)

  const dataset: Dataset = (result.data as unknown[]).map((row, rowIndex) => {
    if (typeof row !== 'object' || row === null) {
      throw new Error(`Invalid CSV row at index ${rowIndex}`)
    }

    const record = row as Record<string, unknown>
    const alternativeValue = record[alternativeKey]

    if (!isString(alternativeValue)) {
      throw new Error(`Alternative value is not a string for row ${rowIndex}`)
    }

    const values = criteriaKeys.map((key) => {
      const cell = record[key]
      if (!isNumber(cell)) {
        throw new Error(`Criterion "${key}" is not numeric for row ${rowIndex}`)
      }
      return cell
    })

    return {
      alternative: alternativeValue,
      values: values,
    }
  })

  return buildProjectData(dataset, criteriaKeys, alternativeKey)
}

export function processExcelResult(data: (string | number)[][]): ProcessedProjectData {
  const fields = data[0] as string[]
  if (!Array.isArray(fields) || fields.length === 0 || !isString(fields[0])) {
    throw new Error('Invalid Excel header row.')
  }

  const alternativeKey = fields[0]
  const criteriaKeys: string[] = fields.slice(1)

  const dataset: Dataset = data.slice(1).map((row, rowIndex) => {
    if (!Array.isArray(row) || row.length < 1 || !isString(row[0])) {
      throw new Error(`Invalid row ${rowIndex + 1} in Excel.`)
    }
    const values = row.slice(1).map((value, colIndex) => {
      if (!isNumber(value)) {
        throw new Error(`Invalid value in row ${rowIndex + 1}, column ${colIndex + 2}.`)
      }
      return value
    })
    return {
      alternative: row[0],
      values: values,
    }
  })

  return buildProjectData(dataset, criteriaKeys, alternativeKey)
}
