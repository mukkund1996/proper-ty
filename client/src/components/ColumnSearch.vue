<script setup lang="ts">
import { ref, defineEmits } from 'vue';
import Dropdown from 'primevue/dropdown';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import InputText from 'primevue/inputtext';
import type { SearchKey } from '@/shared/types';

const props = defineProps<{
  loading: boolean;
}>();

const emit = defineEmits(['search']);
const searchValue = ref();
const searchKey = ref();
const searchOptions = ref<SearchKey[]>(['address', 'class', 'usage', 'area', 'marketValue']);

const clearValues = () => {
  searchValue.value = '';
  searchKey.value = '';
};

const refreshLoad = () => {
  clearValues();
  emit('search', undefined);
};
</script>

<template>
  <div class="form-container">
    <i class="pi pi-refresh" @click="clearValues"></i>
    <Dropdown
      v-model="searchKey"
      :options="searchOptions"
      placeholder="Search by field"
      checkmark
      :highlightOnSelect="false"
      class="w-full md:w-10rem"
    />
    <IconField iconPosition="right">
      <InputIcon>
        <i
          v-if="searchValue?.length && searchKey?.length"
          :class="props.loading ? 'pi pi-spin pi-spinner' : 'pi pi-search'"
          @click="$emit('search', { key: searchKey, value: searchValue })"
        ></i>
      </InputIcon>
      <InputText v-model="searchValue" placeholder="Keyword Search" />
    </IconField>
    <i class="pi pi-times" @click="refreshLoad"></i>
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
