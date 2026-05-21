import type { Chart } from 'chart.js'

export function saveChart(chart: Chart, fileName: string, isDark: boolean) {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const options = chart.options as any
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const originalOptions = JSON.parse(JSON.stringify(chart.options)) as any

  options.plugins.title.color = '#1e293b'
  options.plugins.legend.labels.color = '#1e293b'
  options.scales.x.ticks.color = '#1e293b'
  options.scales.x.grid.color = '#e2e8f0'
  options.scales.x.title.color = '#1e293b'
  options.scales.y.ticks.color = '#1e293b'
  options.scales.y.grid.color = '#e2e8f0'
  options.scales.y.title.color = '#1e293b'
  chart.update('none')

  const canvas = chart.canvas
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  ctx.save()
  ctx.globalCompositeOperation = 'destination-over'
  ctx.fillStyle = '#ffffff'
  ctx.fillRect(0, 0, canvas.width, canvas.height)
  ctx.restore()

  const formatType = 'image/png'
  const base64 = chart.toBase64Image(formatType, 1.0)
  const link = document.createElement('a')
  link.href = base64
  link.download = `${fileName}.png`
  link.click()

  // restore original options
  chart.options = originalOptions

  chart.update('none')
}
