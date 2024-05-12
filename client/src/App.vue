<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <header>
    <div>
      <nav class="nav-container">
        <RouterLink to="/dashboard"><i class="pi pi-home nav-items"></i></RouterLink>
        <h1>Proper-Ty</h1>
        <RouterLink to="/favorites"><i class="pi pi-bookmark nav-items"></i></RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<style scoped>
.nav-items {
  font-size: 2.5rem;
  padding: 0 1.5rem;
  margin: 0 10rem;
}

.nav-container {
  display: flex;
  width: 100%;
  position: fixed;
  top: 25px;
  justify-content: center;
  align-items: center;
}
</style>
