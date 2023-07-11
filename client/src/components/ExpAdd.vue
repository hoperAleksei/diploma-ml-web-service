<template>
  <v-card
      class="mx-auto w-auto ma-2"
      max-width="700"

  >
    <v-card-text>
      <v-form ref="form" validate-on="submit" @submit.prevent="">
        <v-text-field
            v-model="name"
            label="Провести эксперимент"
            placeholder="Название эксперимента"
            append-inner-icon="mdi-plus-circle"
            :rules="rules"
            @click:append-inner="submit"
            @keyup.enter="submit"
        ></v-text-field>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>

import store from "@/store";
import router from "@/router";

export default {
  name: 'ExpAdd',
  computed: {
    state: () => {
      return {state: store.state.state, name: store.state.expName}
    },
  },
  data: (vm) => ({
    name: '',
    rules: [
      value => {
        if (!value) {
          return 'Введите название эксперимента'
        }
        return true
      }
    ],
  }),
  methods: {
    async submit(event) {
      await store.dispatch('updateState')
      if (store.state.state !== 'ready') {
        router.push('/')
      }
      let res = await store.dispatch('createExp', {name: this.name})

      if (res) {
        console.log(1)
        await store.dispatch('updateState')
        store.commit('setExpName', this.name)
        router.push('/datasets')
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
