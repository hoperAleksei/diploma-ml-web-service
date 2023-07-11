<template>
  <v-card class="d-flex">
    <v-form class="d-flex flex-column w-50 justify-start pa-2" @submit.prevent="submit">
      <v-file-input
          v-model="file"
          ref="file"
          accept=".py"
          label="Выберите файл"
          placeholder="Выберите файл"
          prepend-icon="mdi-paperclip"
          style="max-height: 70px"
          hide-details
      ></v-file-input>

      <v-btn type="submit"
             color="orange"
             :loading="loading"
             class="mx-10"
      >Загрузить
      </v-btn>

      <v-card :text="details"
              class="ma-5"
      ></v-card>
    </v-form>

    <v-card class="d-flex flex-wrap w-50 pa-5">
      <v-card v-for="alg in algs"
              :title="alg.name"
              :text="alg.description"
              style="max-width: 250px"
              class="ma-2"
      ></v-card>
    </v-card>
  </v-card>
</template>

<script>
import store from "@/store";

export default {
  name: 'AdminView',
  data() {
    return {
      file: null,
      algs: [],
      loading: false,
      details: '',
    }
  },
  methods: {
    async updataAlgs() {
      const res = await store.dispatch("getAllAlgs")
      this.algs = res
    },
    async submit() {
      this.loading = true
      this.details = ""
      const res = await store.dispatch('uploadAlgFile', {file: this.$refs.file.files[0]})
      if (res.status) {
        this.file = null
        await this.updataAlgs()

      } else {
        this.details = res.detail
      }
      this.loading = false
    }
  },
  mounted() {
    this.updataAlgs()
  }
}
</script>

<style scoped>

</style>
