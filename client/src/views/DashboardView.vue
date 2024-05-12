<script setup lang="ts">
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { LOGIN_ROUTE } from '../router/routes.constant';
import { getAuthKey } from '@/shared/auth';
import { getProperties } from '@/shared/api';

const router = useRouter();

onMounted(async () => {
  if (!getAuthKey()) {
    router.push(LOGIN_ROUTE);
  }
  const propertyResponse = await getProperties(1, 2);
  console.log(propertyResponse);
});
</script>

<template>
  <main>
    <h1>Dashboard</h1>
  </main>
</template>

<style></style>
