<script setup lang="ts">
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { LOGIN_ROUTE } from '../router/routes.constant';
import { getAuthKey } from '@/utils/auth';

const router = useRouter();

onMounted(() => {
  if (!getAuthKey()) {
    router.push(LOGIN_ROUTE);
  }
});
</script>

<template>
  <main>
    <h1>Dashboard</h1>
  </main>
</template>

<style></style>
