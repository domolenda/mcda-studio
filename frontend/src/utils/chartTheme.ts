export const CHART_COLORS = {
  light: {
    text: '#1e293b',
    grid: '#e2e8f0',
  },
  dark: {
    text: '#e2e8f0',
    grid: '#334155',
  },
}

export function getChartThemeColors(isDark: boolean) {
  return isDark ? CHART_COLORS.dark : CHART_COLORS.light
}
