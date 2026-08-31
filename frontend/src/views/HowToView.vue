<template>
  <div class="max-w-3xl mx-auto px-6 py-10 flex flex-col gap-8">
    <Card>
      <template #content>
        <h2 class="text-3xl font-bold">How to Use Guide</h2>
        <p class="mt-2">Follow these steps to get started with MCDA Studio and perform MCDA analysis.</p>
      </template>
    </Card>

    <Card>
      <template #content>
        <h2 class="text-xl font-bold">Step 1: Upload Data</h2>
        <p class="mt-2">
          Go to the <strong>Data</strong> tab to upload your data file in CSV, TXT, XLSX, or XLS format.
        </p>
        <p class="mt-2">The file must follow this format:</p>
        <ul class="list-disc list-inside mt-2">
          <li>First Column - list of alternatives</li>
          <li>Remaining Columns - criteria values in numeric format</li>
          <li>First Row - header with column names</li>
        </ul>
        <p class="mt-2">
          To see examples of valid data files, click <a href="https://github.com/domolenda/mcda-studio/tree/main/examples" class="text-primary">
            here
          </a>.
        </p>
        <p class="mt-2">
          After upload, set each criterion as <strong>Profit</strong> (higher is better) or <strong>Cost</strong> (lower is better).
        </p>
      </template>
    </Card>

    <Card>
      <template #content>
        <h2 class="text-xl font-bold">Step 2: Configure Weights</h2>
        <p class="mt-2">
          Go to the <strong>Configure</strong> tab, set the weight for each criterion manually or use the <strong>Equal/Entropy Weights</strong> buttons to automatically assign weights.
        </p>
        <p class="mt-2">Weights must sum to 1</p>
      </template>
    </Card>

    <Card>
      <template #content>
        <h2 class="text-xl font-bold">Step 3: Select Methods</h2>
        <p class="mt-2">
          Choose the number of methods and configure each one or use the default settings.
        </p>
        <p class="mt-2">Available methods:</p>
        <ul class="list-disc list-inside mt-2">
          <li>
            <strong>TOPSIS</strong> - normalization: Vector<span class="text-surface-500">(recommended)</span>
          </li>
          <li>
            <strong>WASPAS</strong> - normalization: Linear<span class="text-surface-500">(recommended)</span>;
            &lambda; &isin; [0.0, 1.0]
            <span class="text-surface-500">(default: 0.5)</span>
          </li>
          <li>
            <strong>VIKOR</strong> - v &isin; [0.0, 1.0]
            <span class="text-surface-500">(default: 0.5)</span>
          </li>
          <li>
            <strong>ARAS</strong> - normalization: Sum<span class="text-surface-500">(recommended)</span>
          </li>
        </ul>
        <p class="mt-2">
          Available normalization methods: Vector, Linear, Sum, Min-Max.
        </p>
        <p class="mt-2">
          You can select the same method multiple times with different parameters to compare configurations.
        </p>
      </template>
    </Card>

    <Card>
      <template #content>
        <h2 class="text-xl font-bold">Step 4: Run Analysis</h2>
        <p class="mt-2">
          Click <strong>Run Analysis</strong> to execute the selected methods and view the results in the <strong>Results</strong> tab.
        </p>
      </template>
    </Card>

    <Card>
      <template #content>
        <h2 class="text-xl font-bold">Results</h2>
        <p class="mt-2">
          The <strong>Results</strong> tab will display the analysis results, including:
        </p>
        <ul class="mt-2">
          <li>Top 3 alternatives per method (bar chart)</li>
          <li>Full ranking table for all methods</li>
          <li>Correlation scatter charts between methods (when 2+ methods are selected)</li>
        </ul>
        <p class="mt-2">
          Each chart can be exported as an PNG using the <strong>Save as PNG</strong> button.
        </p>
      </template>
    </Card>

    <Card>
      <template #content>
        <h2 class="text-xl font-bold">Save &amp; Load</h2>
        <p class="mt-2">
          Use the <strong>Save</strong> button in the navbar to export your current session as a JSON file.
        </p>
        <p class="mt-2">
          Use the <strong>Load</strong> button to restore it later.
        </p>
        <p class="mt-2">
          <strong>Reset</strong> button clears all data and starts a new session.
        </p>
      </template>
    </Card>
  </div>
</template>

<script setup lang="ts">
import Card from 'primevue/card'
</script>
