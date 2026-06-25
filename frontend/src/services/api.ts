import type {
  TOPSISRequest,
  WASPASRequest,
  VIKORRequest,
  WeightsRequest,
  ComparisonRequest,
  RankingMethodsResponse,
  NormalizationMethodsResponse,
  SingleRankingResponse,
  WeightsResponse,
  MultipleResultData,
} from '@/types'

const BASE_URL = import.meta.env.VITE_API_URL

async function fetchJson<T>(url: string, options?: RequestInit): Promise<T> {
  const response = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
    },
  })

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`)
  }

  return response.json() as Promise<T>
}

export async function getRankingMethods() {
  return fetchJson<RankingMethodsResponse>(`${BASE_URL}/methods/ranking`)
}

export async function getNormalizationMethods() {
  return fetchJson<NormalizationMethodsResponse>(`${BASE_URL}/methods/normalization`)
}

export async function rankTopsis(data: TOPSISRequest) {
  return fetchJson<SingleRankingResponse>(`${BASE_URL}/ranking/topsis`, {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export async function rankWaspas(data: WASPASRequest) {
  return fetchJson<SingleRankingResponse>(`${BASE_URL}/ranking/waspas`, {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export async function rankVikor(data: VIKORRequest) {
  return fetchJson<SingleRankingResponse>(`${BASE_URL}/ranking/vikor`, {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export async function getEqualWeights(data: WeightsRequest) {
  return fetchJson<WeightsResponse>(`${BASE_URL}/weights/equal`, {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export async function getEntropyWeights(data: WeightsRequest) {
  return fetchJson<WeightsResponse>(`${BASE_URL}/weights/entropy`, {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export async function getComparisonResults(data: ComparisonRequest) {
  return fetchJson<MultipleResultData>(`${BASE_URL}/comparison`, {
    method: 'POST',
    body: JSON.stringify(data),
  })
}
