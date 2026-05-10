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

export async function getRankingMethods() {
  const response = await fetch(`${BASE_URL}/methods/ranking`)

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`)
  }

  return response.json() as Promise<RankingMethodsResponse>
}

export async function getNormalizationMethods() {
  const response = await fetch(`${BASE_URL}/methods/normalization`)

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`)
  }

  return response.json() as Promise<NormalizationMethodsResponse>
}

export async function rankTopsis(data: TOPSISRequest) {
  const response = await fetch(`${BASE_URL}/ranking/topsis`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`)
  }

  return response.json() as Promise<SingleRankingResponse>
}

export async function rankWaspas(data: WASPASRequest) {
  const response = await fetch(`${BASE_URL}/ranking/waspas`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`)
  }

  return response.json() as Promise<SingleRankingResponse>
}

export async function rankVikor(data: VIKORRequest) {
  const response = await fetch(`${BASE_URL}/ranking/vikor`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`)
  }

  return response.json() as Promise<SingleRankingResponse>
}

export async function getEqualWeights(data: WeightsRequest) {
  const response = await fetch(`${BASE_URL}/weights/equal`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`)
  }

  return response.json() as Promise<WeightsResponse>
}

export async function getEntropyWeights(data: WeightsRequest) {
  const response = await fetch(`${BASE_URL}/weights/entropy`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`)
  }

  return response.json() as Promise<WeightsResponse>
}

export async function getComparisonResults(data: ComparisonRequest) {
  const response = await fetch(`${BASE_URL}/comparison`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`)
  }

  return response.json() as Promise<MultipleResultData>
}
