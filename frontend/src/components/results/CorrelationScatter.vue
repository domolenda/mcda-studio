<template>
  <div class="flex flex-wrap gap-4 justify-center">
    <div
      v-for="(correlation, i) in correlationsData"
      :key="i"
      class="border border-surface-200 dark:border-surface-700 rounded-lg p-4 bg-white dark:bg-surface-900 w-[420px]"
    >
      <Scatter :data="correlation.chartData" :options="correlation.chartOptions" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { useResultsStore } from '@/stores/resultsStore'
import { useTheme } from '@/composables/useTheme'

import { Scatter } from 'vue-chartjs'
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
  Title,
} from 'chart.js'

import { computed } from 'vue'

const resultsStore = useResultsStore()
const { isDark } = useTheme()

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend, Title)

const correlationsData = computed(
  () =>
    resultsStore.results?.correlations.map((correlation) => {
      const rankings_a = resultsStore.results!.rankings[correlation.method_a]
      const rankings_b = resultsStore.results!.rankings[correlation.method_b]
      const textColor = isDark.value ? '#e2e8f0' : '#1e293b'
      const gridColor = isDark.value ? '#334155' : '#e2e8f0'

      return {
        chartData: {
          datasets: [
            {
              label: 'perfect correlation',
              type: 'line',
              borderColor: '#94a3b8',
              borderDash: [10, 5],
              pointRadius: 0,
              borderWidth: 2,
              data: [
                { x: 1, y: 1 },
                { x: rankings_a.length, y: rankings_a.length },
              ],
            },
            {
              label: 'alternatives',
              backgroundColor: '#10b981',
              data: rankings_a.map((rank, i) => ({ x: rank, y: rankings_b[i] })),
            },
          ],
        },
        chartOptions: {
          aspectRatio: 1,
          plugins: {
            title: {
              color: textColor,
              display: true,
              text: `rw: ${correlation.rw} | WS: ${correlation.ws}`,
              font: { size: 18 },
            },
            legend: {
              labels: {
                color: textColor,
                filter: (item) => item.text !== 'perfect correlation',
              },
            },
          },
          scales: {
            x: {
              ticks: { color: textColor },
              grid: { color: gridColor },
              title: {
                display: true,
                text: correlation.method_a.toUpperCase(),
                font: { size: 16 },
                color: textColor,
              },
            },
            y: {
              ticks: { color: textColor },
              grid: { color: gridColor },
              title: {
                display: true,
                text: correlation.method_b.toUpperCase(),
                font: { size: 16 },
                color: textColor,
              },
            },
          },
        },
      }
    }) ?? [],
)
</script>
