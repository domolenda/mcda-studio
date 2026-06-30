export interface DatasetRow {
  alternative: string
  values: number[]
}

export type Dataset = DatasetRow[]

export type CriterionType = 1 | -1 // profit | cost

export type Criterion = {
  name: string
  type: CriterionType
}

export interface ProjectData {
  dataset: Dataset
  criteria: Criterion[]
}

export interface ProcessedProjectData extends ProjectData {
  alternativeKey: string
}
