<script setup lang="ts">
import { RouterView, useRouter } from 'vue-router';
import Button from 'primevue/button';
import { removeAuthKey } from '@/shared/auth';

const router = useRouter();

const logout = () => {
  removeAuthKey();
  router.push('/');
};
</script>

<template>
  <header>
    <div>
      <nav class="nav-container">
        <h1>Proper-Ty</h1>
        <Button
          class="nav-items"
          icon="pi pi-sign-out"
          label="Logout"
          @click="logout"
          :disabled="$route.path === '/'"
        ></Button>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<style scoped>
.nav-items {
  margin: 0 2.5rem;
}

.nav-container {
  display: flex;
  width: 100%;
  position: fixed;
  top: 65px;
  justify-content: center;
  align-items: center;
}
</style>
