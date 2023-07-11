<template>
  <v-card max-width="700"
          class="ma-auto pa-3">
    <v-card-title>
      {{ name }}
    </v-card-title>
    <v-card-subtitle
        class="mb-5">
      {{ role }}
    </v-card-subtitle>
    <v-card title="Эксперименты"
            max-width="600"
            class="ma-auto">
      <exp-list></exp-list>
    </v-card>
  </v-card>
</template>

<script>
import ExpList from "@/components/ExpList.vue";
import store from "@/store";

export default {
  name: "ProfileView",
  components: {ExpList},
  computed: {
    name() {
      return store.state.username
    },
    role() {
      return (store.state.role === 'admin' ? 'Администратор' : 'Пользователь')
    }
  }
}
</script>

<style scoped>

</style>
