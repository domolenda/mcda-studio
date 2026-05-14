<template>
  <div class="flex justify-center mt-2">
    <div
      class="border border-surface-200 dark:border-surface-700 rounded-lg p-4 font-bold flex flex-col gap-2 w-fit"
    >
      <span>Number of methods</span>
      <Select
        v-model="selectedMethodCount"
        :options="methodCountOptions"
        placeholder="Select..."
        class="w-full"
        @change="handleMethodCountChange"
      />
    </div>
  </div>

  <div class="flex justify-center mt-2" v-if="methodBlocks">
    <div class="flex flex-wrap gap-4">
      <div
        v-for="block in methodBlocks"
        :key="block.id"
        class="border border-surface-200 dark:border-surface-700 rounded-lg p-4 font-bold flex flex-col gap-2 w-fit"
      >
        <span>Method {{ block.id + 1 }}</span>
        <Select
          v-model="block.selectedMethod"
          :options="methodNames"
          placeholder="Select..."
          class="w-full"
          @change="handleMethodChange(block)"
        />
        <div v-if="block.selectedMethod">
          <div v-if="rankingMethods.find((m) => m.name === block.selectedMethod)">
            <div v-if="block.selectedNormalization">
              <span>Normalization method</span>
              <Select
                v-model="block.selectedNormalization"
                :options="normalizationMethods"
                optionLabel="name"
                optionValue="id"
                placeholder="Select..."
                class="w-full"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Select from 'primevue/select'
// import { useDataStore } from '@/stores/dataStore'
// import { useConfigStore } from '@/stores/configStore'
import { computed, ref, onMounted } from 'vue'

import { getRankingMethods, getNormalizationMethods } from '@/services/api'
import type {
  RankingMethod,
  NormalizationMethod,
  RankingMethodsResponse,
  NormalizationMethodsResponse,
} from '@/types'

const rankingMethods = ref<RankingMethod[]>([])
const normalizationMethods = ref<NormalizationMethod[]>([])

const methodCountOptions = computed<number[]>(() => {
  return rankingMethods.value.map((_, i) => i + 1)
})
const selectedMethodCount = ref<number | null>(null)
const methodBlocks = ref<
  { id: number; selectedMethod: string | null; selectedNormalization: string | null }[]
>([])

const methodNames = computed<string[]>(() => {
  return rankingMethods.value.map((method) => method.name)
})

const fetchData = async () => {
  try {
    const rankingResponse: RankingMethodsResponse = await getRankingMethods()
    const normalizationResponse: NormalizationMethodsResponse = await getNormalizationMethods()
    rankingMethods.value = rankingResponse.methods
    normalizationMethods.value = normalizationResponse.normalizations
  } catch (error) {
    console.error(error)
  }
}

function handleMethodCountChange() {
  if (selectedMethodCount.value === null) return
  methodBlocks.value = Array.from({ length: selectedMethodCount.value }, (_, i) => ({
    id: i,
    selectedMethod: null,
    selectedNormalization: null,
  }))
  console.log(rankingMethods.value)
}

function handleMethodChange(block: {
  id: number
  selectedMethod: string | null
  selectedNormalization: string | null
}) {
  if (block.selectedMethod === null) return
  const method = rankingMethods.value.find((m) => m.name === block.selectedMethod)
  block.selectedNormalization = method?.default_normalization ?? null
}

onMounted(() => {
  fetchData()
})
</script>
