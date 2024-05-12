<script setup lang="ts">
import type { PropertyTableRow } from '@/models/property';
import { defineProps, ref } from 'vue';
import DataTable from 'primevue/datatable';
import type { DataTableRowSelectEvent } from 'primevue/datatable';
import Column from 'primevue/column';
const props = defineProps<{
  properties: PropertyTableRow[];
  loading: boolean;
  pageSize: number;
}>();
const emit = defineEmits(['selected', 'unselected']);

const metaKey = ref(true);
const selectedRow = ref();
const columns = [
  { id: 1, field: 'fullAddress', header: 'Address' },
  { id: 2, field: 'classDescription', header: 'Class' },
  { id: 3, field: 'estimatedMarketValue', header: 'Market Value' },
  { id: 4, field: 'buildingArea', header: 'Building Area' },
  { id: 5, field: 'buildingUse', header: 'Building Usage' },
];
const onRowSelect = (event: DataTableRowSelectEvent) => {
  emit('selected', event.data.id);
};
const onRowUnselect = () => {
  emit('unselected');
};
</script>

<template>
  <div class="card">
    <DataTable
      :value="props.properties"
      :loading="props.loading"
      v-model:selection="selectedRow"
      selectionMode="single"
      dataKey="id"
      tableStyle="max-width: 75rem"
      showGridlines
      paginator
      :metaKeySelection="metaKey"
      :rows="props.pageSize"
      :rowsPerPageOptions="[5, 10]"
      @row-select="onRowSelect"
      @row-unselect="onRowUnselect"
    >
      <Column
        v-for="column in columns"
        sortable
        :field="column.field"
        :header="column.header"
        :key="column.id"
      ></Column>
    </DataTable>
  </div>
</template>
