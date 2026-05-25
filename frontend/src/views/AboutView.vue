<template>
  <div class="max-w-3xl mx-auto px-6 py-10 flex flex-col gap-8">
    <Card>
      <template #content>
        <h2 class="text-3xl font-bold">About</h2>
        <p class="mt-2">
          MCDA-studio is a web application for multi-criteria decision analysis (MCDA/MCDM).
        </p>
        <p class="mt-2">Its main features include:</p>
        <ul class="list-disc list-inside mt-2">
          <li>Data import</li>
          <li>Method configuration (TOPSIS, VIKOR, WASPAS)</li>
          <li>Ranking generation</li>
          <li>Visualization and comparison of results</li>
        </ul>
      </template>
    </Card>
    <Card>
      <template #content>
        <h2 class="text-3xl font-bold">Technologies</h2>
        <ul class="list-disc list-inside mt-2">
          <li>
            Back-End
            <ul class="list-disc list-inside ml-4">
              <li>Python 3.13+</li>
              <li>FastAPI</li>
              <li>uv</li>
            </ul>
          </li>
          <li>
            Front-End
            <ul class="list-disc list-inside ml-4">
              <li>Node.js 20+</li>
              <li>Vue 3 + TypeScript</li>
              <li>bun</li>
            </ul>
          </li>
        </ul>
      </template>
    </Card>
    <Card>
      <template #content>
        <h2 class="text-3xl font-bold">Author</h2>
        <p class="mt-2">Dominik Molenda</p>
        <p class="mt-2">
          <a href="https://github.com/domolenda" class="text-primary hover:brightness-110">
            GitHub profile
          </a>
        </p>
      </template>
    </Card>
  </div>
</template>

<script setup lang="ts">
import Card from 'primevue/card'
</script>
