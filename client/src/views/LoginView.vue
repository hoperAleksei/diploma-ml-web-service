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

  <v-form ref="form" validate-on="submit" @submit.prevent="submit">
    <v-card
        class="mx-auto pa-12 pb-8"
        elevation="8"
        max-width="448"
        rounded="lg"
    >
      <div class="text-subtitle-1 text-medium-emphasis">Имя пользователя</div>

      <v-text-field
          v-model="username"
          :rules="rules_username"
          density="compact"
          placeholder="admin"
          prepend-inner-icon="mdi-account"
          variant="outlined"
      ></v-text-field>

      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
        Пароль
      </div>

      <v-text-field
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          :rules="rules_password"
          v-model="password"
          density="compact"
          placeholder="admin"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
          @click:append-inner="visible = !visible"
      ></v-text-field>
      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between" v-if="register">
        Повторите пароль
      </div>

      <v-text-field
          v-if="register"
          :rules="rules_password"
          type="password"
          v-model="password_repeat"
          density="compact"
          placeholder="admin"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
      ></v-text-field>

      <v-btn
          v-if="!register"
          block
          class="mb-8"
          color="blue"
          size="large"
          variant="tonal"
          :loading="loading"
          type="submit"
      >
        Войти
      </v-btn>
      <v-btn
          v-if="register"
          block
          class="mb-8"
          color="red"
          size="large"
          variant="tonal"
          :loading="loading"
          type="submit"
      >
        Зарегистрироваться
      </v-btn>

      <v-card-text class="text-center">
        <a
            class="text-blue text-decoration-none pointer"
            @click="register=!register"
            rel="noopener noreferrer"
            target="_blank"
        >
          {{ register ? 'Войти' : 'Зарегистрироваться' }}
          <v-icon icon="mdi-chevron-right"></v-icon>
        </a>
      </v-card-text>
    </v-card>
  </v-form>
</template>
<script>
import store from "@/store";
import router from "@/router";

export default {
  data: (vm) => ({
    message: '',
    dialog: false,
    loading: false,
    visible: false,
    username: '',
    password: '',
    password_repeat: '',
    register: false,
    rules_username: [
      value => {
        if (value.length < 4 || value.length > 16) {
          return 'Логин должен быть от 4 до 16 символов'
        } else {
          return true
        }
      }
    ],
    rules_password: [
      value => {
        if (value < 5) {
          return 'Пароль должен быть от 5 символов'
        } else {
          return true
        }
      },
      value => {
        if (vm.register && (vm.password !== vm.password_repeat)) {
          return 'Пароли не совпадают'
        } else {
          return true
        }
      },
    ]
  }),
  methods: {
    async submit(event) {
      this.loading = true
      const {valid} = await this.$refs.form.validate()
      if (valid) {
        try {
          if (this.register) {
            await store.dispatch('register', {username: this.username, password: this.password})
          } else {
            await store.dispatch('login', {username: this.username, password: this.password})
          }
          router.push('/profile')
        } catch (e) {
          if (this.register) {
            this.message = 'Такой пользователь уже зарегистрирован'
          } else {
            this.message = 'Неверный логин или пароль'
          }
          this.dialog = true
        }
      }
      this.loading = false
    },
  }
}
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
</style>
