<template>
  <header class="w-full border-b border-gray-700 bg-slate-800">
    <div class="mx-auto max-w-[1800px] px-6 py-3 flex items-center justify-between">
      <nav class="flex items-center gap-6">
        <RouterLink
          v-for="item in NAV_ITEMS"
          :key="item.name"
          class="text-gray-300 hover:text-primary transition-colors [&.router-link-active]:text-primary [&.router-link-active]:font-semibold"
          :to="{ name: item.name }"
        >
          {{ item.title }}</RouterLink
        >
      </nav>
      <div class="flex items-center gap-2">
        <input ref="fileInput" type="file" accept=".json" class="hidden" @change="onFileSelected" />
        <Button
          @click="handleLoadButtonClick"
          size="small"
          label="Load"
          icon="pi pi-upload"
          class="bg-primary border-primary hover:brightness-110"
        />
        <Button
          @click="handleSaveButtonClick"
          size="small"
          label="Save"
          icon="pi pi-save"
          class="bg-primary border-primary hover:brightness-110"
        />
        <Button
          @click="handleResetButtonClick"
          size="small"
          label="Reset"
          icon="pi pi-refresh"
          severity="danger"
          class="hover:brightness-110"
        />
        <Button
          @click="toggleTheme"
          size="small"
          :icon="isDark ? 'pi pi-sun' : 'pi pi-moon'"
          class="bg-primary border-primary hover:brightness-110"
        />
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { useTheme } from '@/composables/useTheme'
import { useRouter } from 'vue-router'
import { ref } from 'vue'

import { showToast } from '@/utils/toastUtils'

import Button from 'primevue/button'

import { saveStateSnapshot, resetStoreState, loadStateSnapshot } from '@/utils/stateSnapshot'

const { isDark, toggleTheme } = useTheme()
const fileInput = ref<HTMLInputElement | null>(null)

const router = useRouter()
const NAV_ITEMS = router.options.routes
  .filter((route) => route.meta?.showInMenu === true)
  .map((route) => ({
    name: route.name as string,
    title: route.meta?.title as string,
  }))

function handleSaveButtonClick() {
  try {
    saveStateSnapshot()
    showToast('State snapshot saved successfully', 'success', 'Snapshot saved')
  } catch {
    showToast('Failed to save state snapshot')
  }
}

function handleLoadButtonClick() {
  fileInput.value?.click()
}

function onFileSelected(event: Event) {
  try {
    const input = event.target as HTMLInputElement
    const file = input.files?.[0]
    if (file) {
      loadStateSnapshot(file)
      input.value = ''
      showToast('State snapshot loaded successfully', 'success', 'Loaded')
    }
  } catch {
    showToast('Failed to load state snapshot')
  }
}

function handleResetButtonClick() {
  try {
    resetStoreState()
    showToast('Data cleared successfully', 'success', 'Cleared')
  } catch {
    showToast('Failed to clear data')
  }
}
</script>

<style scoped></style>
