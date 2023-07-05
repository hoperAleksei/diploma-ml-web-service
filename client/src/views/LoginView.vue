<template>
  <div>
    <input v-model="username" placeholder="username">
    <input v-model="password" placeholder="password">
    <button @click="login">login</button>
    <button @click="register">register</button>

  </div>
</template>

<script>
import router from "@/router";
import store from "@/store";

export default {
  name: "LoginView",
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async login(event) {
      await store.dispatch('login', {username: this.username, password: this.password})
      router.push('/profile')
    },
    async register(event) {
      await store.dispatch('register', {username: this.username, password: this.password})
      router.push('/profile')
    }
  }
}
</script>

<style scoped>

</style>