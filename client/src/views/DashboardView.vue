<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

import PropertyTable from '@/components/PropertyTable.vue';
import ColumnSearch from '@/components/ColumnSearch.vue';

import { LOGIN_ROUTE } from '../router/routes.constant';
import { getAuthKey } from '@/shared/auth';
import { getProperties } from '@/shared/api';
import type { PropertyTableRow } from '@/models/property';
import type { SearchKeyValue } from '@/shared/types';
import { extractPropertyTableData } from '@/models/property';
import { DEFAULT_LOADING_DELAY, DEFAULT_PAGE_LIMIT, DEFAULT_PAGE_COUNT } from '@/shared/constants';

const router = useRouter();

const pageIsLoading = ref(true);

const properties = ref([] as PropertyTableRow[]);

const loadData = async (searchTerm?: SearchKeyValue) => {
  pageIsLoading.value = true;
  const propertyResponse = await getProperties(DEFAULT_PAGE_LIMIT, searchTerm);
  if (propertyResponse) {
    properties.value = propertyResponse.properties.map(extractPropertyTableData);
    setTimeout(() => (pageIsLoading.value = false), DEFAULT_LOADING_DELAY);
  }
};

onMounted(async () => {
  if (!getAuthKey()) {
    router.push(LOGIN_ROUTE);
  }
  loadData();
});
</script>

<template>
  <main>
    <div class="dashboard-container">
      <ColumnSearch
        @search="(searchKeyValue) => loadData(searchKeyValue as SearchKeyValue)"
        :loading="pageIsLoading"
      ></ColumnSearch>
      <PropertyTable
        :properties="properties"
        :loading="pageIsLoading"
        :pageSize="DEFAULT_PAGE_COUNT"
      ></PropertyTable>
    </div>
  </main>
</template>

<style scoped>
.dashboard-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  gap: 1.5rem;
}
</style>
