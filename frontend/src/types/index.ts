export interface DatasetRow {
  alternative: string
  values: number[]
}

export type CriterionType = 1 | -1 // profit | cost

export type Dataset = DatasetRow[]

export type Criterion = {
  name: string
  type: CriterionType
}

export interface ProjectData {
  dataset: Dataset
  criteria: Criterion[]
}

export type Params = {
  name: string
  value: number | string | null
}

export interface ConfigData {
  name: string
  params: Params[]
}

export type CorrelationData = {
  method_a: string
  method_b: string
  rw: number
  ws: number
}

export interface MultipleResultData {
  rankings: {
    [method: string]: number[]
  }
  correlations: CorrelationData[]
}
