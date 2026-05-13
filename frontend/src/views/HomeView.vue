<template>
  <div class="flex flex-col items-center justify-center text-center px-4 min-h-[calc(100vh-4rem)]">
    <h2 class="text-2xl font-medium text-surface-500 dark:text-surface-400 uppercase mb-2">
      Welcome to
    </h2>
    <h1 class="text-7xl font-black text-primary">MCDA Studio</h1>
    <RouterLink :to="{ name: 'data' }" class="mt-8">
      <Button
        size="large"
        class="px-8 py-4 text-lg font-bold shadow-lg bg-emerald-500 text-white border-emerald-500 hover:shadow-primary-600 hover:brightness-110 transition-all"
      >
        Get Started
      </Button>
    </RouterLink>
  </div>
</template>

<script setup lang="ts">
import Button from 'primevue/button'
</script>
