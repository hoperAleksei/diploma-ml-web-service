<template>
  <nav v-if="isAuth">
    <router-link to="/">Создать</router-link>
    |
    <router-link v-if="isAdmin" to="/admin">Администрирование</router-link>
    |
    <router-link to="/profile"> {{ getUsername }}</router-link>
    |
    <button @click="btnLogout">Выйти</button>
  </nav>
  <!--  <LoginForm></LoginForm>-->
  <router-view/>
</template>
<script>
import store from "@/store";
import router from "@/router";
import LoginForm from "@/components/LoginForm.vue";

export default {
  components: {LoginForm},
  computed: {
    isAuth: () => {
      return store.state.isAuth
    },
    isAdmin: () => {
      return store.state.role === 'admin';
    },
    getUsername: () => {
      return store.state.username
    }
  },
  methods: {
    store,
    btnLogout() {
      store.dispatch('logout')
      router.push('/')
    }
  }
}
</script>


<style>

</style>
