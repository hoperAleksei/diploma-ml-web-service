<template>
  <v-app>
    <v-navigation-drawer v-model="sidebar" temporary v-if="isAuth">
      <v-list>
        <v-list-item :to="'/admin'" v-if="isAdmin">
          <v-list-item-title>
            <v-icon left dark>mdi-application-edit</v-icon>
            Администрирование
          </v-list-item-title>
        </v-list-item>
        <v-list-item :to="'/profile'">
          <v-list-item-title>
            <v-icon left dark>mdi-account</v-icon>
            {{ username }}
          </v-list-item-title>
        </v-list-item>
        <v-list-item :key="logout" title="Выйти" @click="logout"></v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app v-if="isAuth" color="orange">
      <v-app-bar-nav-icon class="d-flex d-sm-none" @click="sidebar = !sidebar"></v-app-bar-nav-icon>
      <v-toolbar-title>
        <router-link to="/" class="head-text">
          {{ mainName }}
        </router-link>
        <v-btn v-if="mainName !== 'Эксперименты'" density="compact" icon="mdi-close" @click="cancelExp"></v-btn>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="d-none d-sm-flex">
        <v-btn
            flat
            :to="'/admin'"
            v-if="isAdmin">
          <v-icon left dark>mdi-application-edit</v-icon>
          Администрирование
        </v-btn>
        <v-btn
            flat
            :to="'/profile'">
          <v-icon left dark>mdi-account</v-icon>
          {{ username }}
        </v-btn>
        <v-btn
            flat
            :key="'logout'"
            @click="logout">
          <v-icon left dark>{{ 'mdi-logout' }}</v-icon>
          Выйти
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>
<script>
import store from "@/store";
import router from "@/router";

export default {
  name: 'Application',
  computed: {
    isAuth: () => {
      return store.state.isAuth
    },
    isAdmin: () => {
      return store.state.role === 'admin';
    },
    username: () => {
      return store.state.username
    },
    mainName: () => {
      if (store.state.expName === '') {
        return 'Эксперименты'
      } else {
        return store.state.expName
      }
    }
  },
  data() {
    return {
      sidebar: false,
    }
  },
  methods: {
    logout: () => {
      store.dispatch('logout')
      router.push('/login')
    },
    cancelExp: async () => {
      let res = await store.dispatch('cancelExp')
      if (res) {
        router.push('/')
      }
    }
  },

}
</script>


<style>
.head-text{
font-family: "Roboto", sans-serif;
  text-decoration: none;
  color: black;
  outline: none;
}
</style>
