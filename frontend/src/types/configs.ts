export type Params = {
  name: string
  value: number | string | null
}

export interface ConfigData {
  id: string
  name: string
  params: Params[]
}

export interface ParamEntry {
  name: string
  value: number | string
}

export interface MethodBlock {
  id: number
  methodId: string | null
  selectedMethod: string | null
  selectedNormalization: string | null
  parameters: {
    name: string
    label: string
    value: number
    min: number
    max: number
    default: number
  }[]
}

export interface TableRow {
  type: string
  [key: string]: string | number
}
