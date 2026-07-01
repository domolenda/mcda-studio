import type { ConfigData } from './configs'

export interface BaseRankingRequest {
  matrix: number[][]
  types: number[]
  weights: number[]
}

export interface TOPSISRequest extends BaseRankingRequest {
  normalization_method?: string | null
}

export interface WASPASRequest extends BaseRankingRequest {
  normalization_method?: string | null
  lambda_?: number
}

export interface VIKORRequest extends BaseRankingRequest {
  v?: number
}

export interface WeightsRequest {
  matrix: number[][]
}

export interface ComparisonRequest extends BaseRankingRequest {
  methods_config: ConfigData[]
}

export interface MethodParameter {
  name: string
  type: string
  default: number
  min: number
  max: number
}

export interface RankingMethod {
  id: string
  name: string
  normalization: boolean
  default_normalization: string | null
  parameters: MethodParameter[]
}

export interface RankingMethodsResponse {
  methods: RankingMethod[]
}

export interface NormalizationMethod {
  id: string
  name: string
}

export interface NormalizationMethodsResponse {
  normalizations: NormalizationMethod[]
}

export interface SingleRankingResponse {
  ranking: number[]
}

export interface WeightsResponse {
  weights: number[]
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
