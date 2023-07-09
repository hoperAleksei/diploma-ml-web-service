<template>
  <v-dialog
      v-model="dialog"
      width="auto"
  >
    <v-card>
      <v-card-text>
        {{ message }}
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" block @click="dialog = false">Закрыть</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
  <v-card
      class="mx-auto w-auto ma-2"
      max-width="700"
  >
    <v-card-text>
      <v-form ref="form" validate-on="submit" @submit.prevent="submit">
        <v-text-field
            v-model="url"
            label="Ссылка на выборку"
            placeholder="Ссылка на выборку"
            :rules="rules_url"
        ></v-text-field>
        <v-file-input
            v-model="file"
            ref="file"
            accept="text/csv"
            label="Выберите файл"
            placeholder="Выберите файл"
            prepend-icon="mdi-paperclip"
            :rules="rules_file">

        </v-file-input>
        <v-btn
            :loading="loading"
            color="primary"
            type="submit">
          Добавить
        </v-btn>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>

import store from "@/store";

export default {
  name: 'DsAdd',
  data: (vm) => ({
    file: null,
    url: '',
    loading: false,
    dialog: false,
    message: '',
    rules_url: [
      value => {
        if (!value && !vm.file) {
          return 'Введите ссылку на выборку'
        }
        return true
      },
      value => {
        if (!vm.file && value && !(/^(https?:\/\/)?([\w\-])+\.{1}([a-zA-Z]{2,63})([\/\w-]*)*\/?\??([^#\n\r]*)?#?([^\n\r]*)$/.test(value))) {
          return 'Это не ссылка'
        }
        return true
      }
    ],
    rules_file: [
      value => {
        if (!value && !vm.name) {
          return 'Укажите файл выборки'
        }
        return true
      },
      value => {
        if (value && value[0].size > 2000000) {
          return 'Размер выборки не должен превышать 2Mb'
        }
        return true
      },
    ],
  }),
  methods: {
    async submit(event) {
      this.loading = true
      if (this.url !== '') {
        let res = await store.dispatch('postDsUrl', {url: this.url})
        if (res.status) {
          this.url = ''
          await this.$parent.$refs.list.getDatasets()
        } else {
          if (res.detail === 'file already exist') {
            this.message = "Файл с таким именем уже существует"
            this.dialog = true
          } else if (res.detail === 'file is not dataset') {
            this.message = "Файл не является выборкой данных"
            this.dialog = true
          } else if (res.detail === 'file not found') {
            this.message = "Файл не удалось загрузить по ссылке"
            this.dialog = true
          }
        }

      } else if (this.file !== null) {
        let res = await store.dispatch('postDsFile', {file: this.$refs.file.files[0]})
        if (res.status) {
          this.file = null
          await this.$parent.$refs.list.getDatasets()

        } else {
          if (res.detail === 'file already exist') {
            this.message = "Файл с таким именем уже существует"
            this.dialog = true
          } else if (res.detail === 'file is not dataset') {
            this.message = "Файл не является выборкой данных"
            this.dialog = true
          }
        }
      }
      this.loading = false
    }
  }
}
</script>

<style scoped>

</style>
