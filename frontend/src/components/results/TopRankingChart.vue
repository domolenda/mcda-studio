<template>
  <div class="flex flex-wrap gap-4 justify-center">
    <div
      v-for="(chart, i) in chartsData"
      :key="i"
      class="border border-surface-200 dark:border-surface-700 rounded-lg p-4 bg-white dark:bg-surface-900 w-85"
    >
      <Bar ref="chartRefs" :data="chart.chartData" :options="chart.chartOptions" />
      <div class="flex justify-center mt-2">
        <Button
          label="Save as PNG"
          size="small"
          @click="handleSaveChart(chartRefs[i], chart.method)"
          class="bg-primary border-primary hover:brightness-110"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useDataStore } from '@/stores/dataStore'
import { useResultsStore } from '@/stores/resultsStore'
import { useTheme } from '@/composables/useTheme'
import { saveChart } from '@/utils/chartExport'
import { getChartThemeColors } from '@/utils/chartTheme'

import Button from 'primevue/button'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend,
  Title,
} from 'chart.js'

import { computed, ref } from 'vue'

const dataStore = useDataStore()
const resultsStore = useResultsStore()
const { isDark } = useTheme()
const chartRefs = ref<Array<InstanceType<typeof Bar> | null>>([])

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend, Title)

const rankings = computed(() => resultsStore.results?.rankings ?? {})
const dataSet = computed(() => dataStore.data?.dataset ?? [])
const alternatives = computed(() => dataSet.value.map((row) => row.alternative))
const methods = computed(() => Object.keys(rankings.value))

const topAlternativesPerMethod = computed(() => {
  const currentRankings = rankings.value
  return Object.fromEntries(
    methods.value.map((method) => {
      const methodRankings = currentRankings[method] ?? []
      const top3Indexes = methodRankings
        .map((rank, idx) => ({ rank, idx }))
        .sort((a, b) => a.rank - b.rank)
        .slice(0, 3)
        .map((item) => item.idx)

      const top3Alternatives = top3Indexes.map((idx) => ({
        alternative: alternatives.value[idx],
        rank: methodRankings[idx] ?? 0,
      }))
      return [method, top3Alternatives]
    }),
  )
})

const chartsData = computed(() => {
  const { text: textColor, grid: gridColor } = getChartThemeColors(isDark.value)

  return Object.entries(topAlternativesPerMethod.value).map(([method, top3]) => ({
    method,
    chartData: {
      labels: top3.map((item) => item.alternative),
      datasets: [
        {
          label: method.toUpperCase(),
          data: top3.map((item) => 4 - item.rank),
          backgroundColor: '#10b981',
        },
      ],
    },
    chartOptions: {
      devicePixelRatio: 2,
      aspectRatio: 1.2,
      plugins: {
        title: {
          color: textColor,
          display: true,
          text: `Top 3 - ${method.toUpperCase()}`,
          font: { size: 18 },
        },
        legend: { display: false },
      },
      scales: {
        x: {
          ticks: { color: textColor },
          grid: { color: gridColor },
        },
        y: {
          ticks: {
            display: false,
          },
          grid: { color: gridColor },
          grace: 1,
        },
      },
    },
  }))
})

function handleSaveChart(ref: InstanceType<typeof Bar> | null | undefined, method: string) {
  if (!ref?.chart) return
  saveChart(ref.chart, `top3_${method.toUpperCase()}`)
}
</script>
