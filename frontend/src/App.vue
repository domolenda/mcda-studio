<script setup lang="ts">
import AppNavbar from '@/components/common/AppNavbar.vue'
import Toast from 'primevue/toast'
</script>

<template>
  <Toast />
  <AppNavbar />
  <div class="min-h-screen bg-surface-100 dark:bg-surface-950">
    <RouterView />
  </div>
</template>

<style scoped></style>
