<template>
  <div>
    <input v-model="username" placeholder="username">
    <input v-model="password" placeholder="password">
    <button @click="auth">login</button>
    <button @click="register">register</button>

  </div>
</template>

<script>
import {getAuth, getReg} from '@/hooks/auth'
import router from "@/router";

export default {
  name: "LoginView",
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async auth(event) {
      await getAuth(this.username, this.password)
      router.push('/profile')
    },
    async register(event) {
      await getReg(this.username, this.password)
      router.push('/profile')
    }
  }
}
</script>

<style scoped>

</style>