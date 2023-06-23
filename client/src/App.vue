<template>
  <nav v-if="getAuth">
    <router-link to="/">Создать</router-link>
    |
    <router-link to="/profile">Профиль</router-link>
    |
    <button @click="btnLogout">Выйти</button>
  </nav>

  <router-view/>
</template>
<script>
import {mapGetters} from 'vuex'
import {getAuth, logout} from "@/hooks/auth";
import router from "@/router";

export default {
  computed: {
    ...mapGetters({
      getAuth: "getAuth"
    })
  },
  methods: {
    btnLogout() {
      logout()
      router.push('/')
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
