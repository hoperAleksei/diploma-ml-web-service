<template>
  <v-form validate-on="submit lazy" @submit.prevent="submit">
    <v-card
        class="mx-auto pa-12 pb-8"
        elevation="8"
        max-width="448"
        rounded="lg"
    >
      <div class="text-subtitle-1 text-medium-emphasis">Имя пользователя</div>

      <v-text-field
          density="compact"
          placeholder="Email address"
          prepend-inner-icon="mdi-account"
          variant="outlined"
      ></v-text-field>

      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
        Пароль
      </div>

      <v-text-field
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          placeholder="Enter your password"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
          @click:append-inner="visible = !visible"
      ></v-text-field>

      <v-btn
          block
          class="mb-8"
          color="blue"
          size="large"
          variant="tonal"
      >
        Войти
      </v-btn>

      <v-card-text class="text-center">
        <a
            class="text-blue text-decoration-none"
            href="#"
            rel="noopener noreferrer"
            target="_blank"
        >
          Зарегистрироваться
          <v-icon icon="mdi-chevron-right"></v-icon>
        </a>
      </v-card-text>
    </v-card>
  </v-form>
</template>
<script>
export default {
  data: () => ({
    visible: false,
  }),
}
</script>