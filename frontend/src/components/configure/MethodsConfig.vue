<template>
  <div class="flex justify-center mt-2">
    <div
      class="border border-surface-200 dark:border-surface-700 rounded-lg p-4 font-bold flex flex-col gap-2 w-fit bg-white dark:bg-surface-900"
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
        class="border border-surface-200 dark:border-surface-700 rounded-lg p-4 font-bold flex flex-col gap-2 w-64 bg-white dark:bg-surface-900"
      >
        <span class="justify-center flex">Method {{ block.id + 1 }}</span>
        <Select
          v-model="block.selectedMethod"
          :options="rankingMethods"
          optionLabel="name"
          optionValue="id"
          placeholder="Select..."
          class="w-full"
          @change="handleMethodChange(block)"
        />
        <div v-if="block.selectedMethod">
          <div v-if="rankingMethods.find((m) => m.id === block.selectedMethod)">
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
            <div v-if="block.parameters">
              <div v-for="param in block.parameters" :key="param.id">
                <span>{{ param.label }}</span>
                <InputNumber
                  v-model="param.value"
                  :min="param.min"
                  :max="param.max"
                  :minFractionDigits="1"
                  :maxFractionDigits="20"
                  :allowEmpty="false"
                  mode="decimal"
                  inputClass="w-full text-center py-1 px-2 border rounded-md dark:bg-surface-900"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Select from 'primevue/select'
import InputNumber from 'primevue/inputnumber'
import { useConfigStore } from '@/stores/configStore'
import { computed, ref, watch, onMounted } from 'vue'

import { getRankingMethods, getNormalizationMethods } from '@/services/api'
import type {
  RankingMethod,
  NormalizationMethod,
  RankingMethodsResponse,
  NormalizationMethodsResponse,
} from '@/types'

const rankingMethods = ref<RankingMethod[]>([])
const normalizationMethods = ref<NormalizationMethod[]>([])
const configStore = useConfigStore()

const methodCountOptions = computed<number[]>(() => {
  return rankingMethods.value.map((_, i) => i + 1)
})
const selectedMethodCount = ref<number | null>(null)
const methodBlocks = ref<
  { id: number; selectedMethod: string | null; selectedNormalization: string | null }[]
>([])

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
  configStore.setSelectedMethodCount(selectedMethodCount.value)
}

function handleMethodChange(block: {
  id: number
  selectedMethod: string | null
  selectedNormalization: string | null
  parameters: Record<string, number>[]
}) {
  if (block.selectedMethod === null) return
  const method = rankingMethods.value.find((m) => m.id === block.selectedMethod)
  block.selectedNormalization = method?.default_normalization ?? null
  block.parameters = (method?.parameters ?? []).map((p) => ({
    ...p,
    value: p.default,
    label: formatParamName(p.name),
  }))
  const paramList = (method?.parameters ?? []).map((p) => ({
    name: p.name,
    value: p.default,
  }))
  if (block.selectedNormalization) {
    paramList.push({
      name: 'normalization_method',
      value: block.selectedNormalization,
    })
  }
  const ConfigBlock = {
    name: block.selectedMethod,
    params: paramList,
  }
  configStore.addMethodConfig(block.id, ConfigBlock)
}

function formatParamName(name: string): string {
  const cleaned = name.endsWith('_') ? name.slice(0, -1) : name
  return cleaned.charAt(0).toUpperCase() + cleaned.slice(1)
}

watch(
  methodBlocks,
  (newConfig) => {
    const mapedConfig = newConfig.map((newConfig) => {
      const paramList = (newConfig.parameters ?? []).map((p) => ({
        name: p.name,
        value: p.value,
      }))
      if (newConfig.selectedNormalization) {
        paramList.push({
          name: 'normalization_method',
          value: newConfig.selectedNormalization,
        })
      }
      return {
        name: newConfig.selectedMethod ?? '',
        params: paramList,
      }
    })
    configStore.setMethodsConfig(mapedConfig)
  },
  { deep: true },
)

onMounted(async () => {
  await fetchData()
  if (configStore.selectedMethodCount) {
    selectedMethodCount.value = configStore.selectedMethodCount
  }
  if (configStore.methodsConfig && configStore.methodsConfig.length > 0) {
    const mapedConfig = configStore.methodsConfig
    methodBlocks.value = mapedConfig.map((config, idx) => ({
      id: idx,
      selectedMethod: config.name,
      selectedNormalization:
        config.params.find((p) => p.name === 'normalization_method')?.value ?? '',
      parameters: config.params.filter((p) => p.name !== 'normalization_method'),
    }))
  }
})
</script>
