export interface ChartExportOptions {
  plugins: {
    title: { color: string }
    legend: { labels: { color: string } }
  }
  scales: {
    x: { ticks: { color: string }; grid: { color: string }; title: { color: string } }
    y: { ticks: { color: string }; grid: { color: string }; title: { color: string } }
  }
}
