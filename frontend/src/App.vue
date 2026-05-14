<script setup lang="ts">
import AppNavbar from '@/components/common/AppNavbar.vue'
</script>

<template>
  <AppNavbar />
  <div class="min-h-screen bg-surface-100 dark:bg-surface-900">
    <RouterView />
  </div>
</template>

<style scoped></style>
