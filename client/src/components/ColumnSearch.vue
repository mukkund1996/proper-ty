<script setup lang="ts">
import { ref } from 'vue';
import Dropdown from 'primevue/dropdown';
import IconField from 'primevue/iconfield';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import type { SearchKey } from '@/shared/types';

const props = defineProps<{
  loading: boolean;
}>();

const emit = defineEmits(['search']);
const searchValue = ref();
const searchKey = ref();
const searchOptions = ref<SearchKey[]>(['address', 'class', 'usage', 'area', 'marketValue']);

const clearValues = () => {
  if (searchValue.value.length && searchKey.value.length) {
    emit('search');
  }
  searchValue.value = '';
  searchKey.value = '';
};
</script>

<template>
  <div class="form-container">
    <Dropdown
      v-model="searchKey"
      :options="searchOptions"
      placeholder="Search by field"
      checkmark
      :highlightOnSelect="false"
      class="w-full md:w-10rem"
    />
    <IconField iconPosition="right">
      <InputText v-model="searchValue" placeholder="Keyword Search" />
    </IconField>
    <Button
      :disabled="!searchValue?.length || !searchKey?.length"
      :icon="props.loading ? 'pi pi-spin pi-spinner' : 'pi pi-search'"
      @click="$emit('search', { key: searchKey, value: searchValue })"
    ></Button>
    <Button icon="pi pi-times" @click="clearValues"></Button>
  </div>
</template>
<style scoped>
.form-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 1.2rem;
}

i {
  cursor: pointer;
}
i:hover {
  color: green;
}
</style>
