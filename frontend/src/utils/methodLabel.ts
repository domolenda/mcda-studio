export function formatMethodLabel(methodId: string, allMethodsId: string[]): string {
  const baseName = methodId.split('_')[0] ?? methodId;
  const count = allMethodsId.filter((id) => id.split('_')[0] === baseName).length
  if (count === 1) {
    return baseName.toUpperCase()
  }
  return `${baseName.toUpperCase()} (${methodId.split('_')[1]})`
}
