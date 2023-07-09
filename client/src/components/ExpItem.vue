<template>
  <v-list-item :key="$props.title">
    <div @click="openExp">
      <v-list-item-title>{{ $props.title }}</v-list-item-title>
      <v-list-item-subtitle>{{ $props.modelCount }} моделей</v-list-item-subtitle>
    </div>
    <template v-slot:append>
      <v-btn icon @click="deleteExp">
        <v-icon>mdi-delete</v-icon>
      </v-btn>
    </template>
  </v-list-item>
</template>

<script>
export default {
  name: 'ExpItem',
  props: {
    title: String,
    modelCount: Number,
  },
  methods: {
    deleteExp(event) {
      console.log('deleteExp', event)
    },
    openExp(event) {
      console.log('openExp', event)
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
