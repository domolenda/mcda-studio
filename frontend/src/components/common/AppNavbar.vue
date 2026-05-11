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
      <Button @click="toggleTheme" severity="secondary" variant="text" rounded>
        {{ isDark ? '☀️' : '🌙' }}
      </Button>
    </div>
  </header>
</template>

<script setup lang="ts">
import { useTheme } from '@/composables/useTheme'
import { useRouter } from 'vue-router'

const { isDark, toggleTheme } = useTheme()

const router = useRouter()
const NAV_ITEMS = router.options.routes
  .filter((route) => route.meta?.showInMenu === true)
  .map((route) => ({
    name: route.name as string,
    title: route.meta?.title as string,
  }))
</script>

<style scoped></style>
