<template>
  <v-sheet max-width="300" class="mx-auto">
    <v-form validate-on="submit lazy" @submit.prevent="submit">
      <v-text-field
          v-model="userName"
          :rules="rules"
          label="User name"
      ></v-text-field>

      <v-btn
          :loading="loading"
          type="submit"
          block
          class="mt-2"
          text="Submit"
      ></v-btn>
    </v-form>
  </v-sheet>
</template>

<script>

import {ref} from 'vue'

export default {
  props: {},
  setup(props) {
    const loading = ref(false)
    const rules = ref([value => checkApi(value)])
    const timeout = ref(null)
    const userName = ref('')

    const submit = async (event) => {
      loading.value = true

      // const results = await event

      loading.value = false

      // alert(JSON.stringify(results, null, 2))
    }
    const checkApi = async (event) => {
      return new Promise(resolve => {
        clearTimeout(timeout.value)

        timeout.value = setTimeout(() => {
          if (!userName.value) return resolve('Please enter a user name.')
          if (userName.value === 'johnleider') return resolve('User name already taken. Please try another one.')

          return resolve(true)
        }, 1000)
      })
    }

    return {loading, rules, timeout, userName, submit}
  }
}
</script>

<style scoped>

</style>