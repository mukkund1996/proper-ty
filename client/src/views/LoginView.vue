<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
import Password from 'primevue/password';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import { createBasicAuthToken, fetchWithBasicAuth, getAuthKey, setAuthKey } from '../shared/auth';
import { DASHBOARD_ROUTE } from '../router/routes.constant';
import { API_URL } from '../shared/constants';

const router = useRouter();

const username = ref('');
const password = ref('');
const incorrectCredentials = ref(false);

const login = async () => {
  incorrectCredentials.value = false;
  const authToken = createBasicAuthToken(username.value, password.value);
  const response = await fetchWithBasicAuth(
    `${API_URL}/authenticate`,
    'GET',
    undefined,
    undefined,
    authToken,
  );
  if (response.ok) {
    incorrectCredentials.value = false;
    setAuthKey(authToken);
    username.value = '';
    password.value = '';
    router.push(DASHBOARD_ROUTE);
  } else {
    incorrectCredentials.value = true;
  }
};

onMounted(() => {
  if (getAuthKey()) {
    router.push(DASHBOARD_ROUTE);
  }
});
</script>

<template>
  <main>
    <div class="form-container">
      <h1>Login</h1>
      <InputGroup class="input">
        <InputGroupAddon>
          <i class="pi pi-user"></i>
        </InputGroupAddon>
        <InputText v-model="username" placeholder="Username" />
      </InputGroup>
      <InputGroup class="input">
        <InputGroupAddon>
          <i class="pi pi-key"></i>
        </InputGroupAddon>
        <Password
          v-model="password"
          placeholder="Password"
          :feedback="false"
          :invalid="incorrectCredentials"
        />
      </InputGroup>
      <Button label="Login" @click="login"></Button>
    </div>
  </main>
</template>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  gap: 1.5rem;
}
.input {
  width: 20%;
}
</style>
