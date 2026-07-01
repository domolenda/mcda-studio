import { useToast } from 'primevue/usetoast'

export function showToast(
  detail: string,
  severity: 'error' | 'success' = 'error',
  summary: string = severity === 'error' ? 'Error' : 'Success',
) {
  const toast = useToast()
  toast.add({
    severity: severity,
    summary: summary,
    detail,
    life: 3000,
  })
}
