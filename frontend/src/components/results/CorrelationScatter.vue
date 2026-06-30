<template>
  <div class="flex flex-wrap gap-4 justify-center">
    <div
      v-for="(correlation, i) in correlationsData"
      :key="i"
      class="border border-surface-200 dark:border-surface-700 rounded-lg p-4 bg-white dark:bg-surface-900 w-105"
    >
      <Chart
        type="scatter"
        ref="chartRefs"
        :data="correlation.chartData"
        :options="correlation.chartOptions"
      />
      <div class="flex justify-center mt-2">
        <Button
          label="Save as PNG"
          size="small"
          @click="
            handleSaveChart(
              chartRefs[i],
              correlation.chartOptions.scales.x.title.text,
              correlation.chartOptions.scales.y.title.text,
            )
          "
          class="bg-primary border-primary hover:brightness-110"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useResultsStore } from '@/stores/resultsStore'
import { useTheme } from '@/composables/useTheme'
import { saveChart } from '@/utils/chartExport'

import Button from 'primevue/button'
import { Chart } from 'vue-chartjs'
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  LineElement,
  LineController,
  Tooltip,
  Legend,
  Title,
} from 'chart.js'

import { computed, ref } from 'vue'

const resultsStore = useResultsStore()
const { isDark } = useTheme()
const chartRefs = ref<Array<InstanceType<typeof Chart> | null>>([])

ChartJS.register(LinearScale, PointElement, LineElement, LineController, Tooltip, Legend, Title)

const correlationsData = computed(
  () =>
    resultsStore.results?.correlations.map((correlation) => {
      const rankings_a = resultsStore.results!.rankings[correlation.method_a] ?? []
      const rankings_b = resultsStore.results!.rankings[correlation.method_b] ?? []
      const textColor = isDark.value ? '#e2e8f0' : '#1e293b'
      const gridColor = isDark.value ? '#334155' : '#e2e8f0'

      return {
        chartData: {
          datasets: [
            {
              label: 'perfect correlation',
              type: 'line' as const,
              borderColor: '#94a3b8',
              borderDash: [10, 5],
              pointRadius: 0,
              borderWidth: 2,
              pointStyle: 'line',
              data: [
                { x: 1, y: 1 },
                { x: rankings_a.length, y: rankings_a.length },
              ],
            },
            {
              label: 'alternatives',
              backgroundColor: '#10b981',
              data: rankings_a.map((rank, i) => ({ x: rank, y: rankings_b[i] ?? null })),
            },
          ],
        },
        chartOptions: {
          devicePixelRatio: 3,
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
                usePointStyle: true,
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

function handleSaveChart(
  ref: InstanceType<typeof Chart> | null | undefined,
  methodA: string,
  methodB: string,
) {
  if (!ref?.chart) return
  saveChart(ref.chart, `correlation_${methodA}_${methodB}`)
}
</script>
