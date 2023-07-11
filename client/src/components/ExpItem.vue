<template>
  <v-list-item @click="openExp">
    <div>
      <v-list-item-title>{{ $props.title }}</v-list-item-title>
    </div>
    <template v-slot:append>
<!--      <v-btn icon @click="deleteExp">-->
<!--        <v-icon>mdi-delete</v-icon>-->
<!--      </v-btn>-->
    </template>
  </v-list-item>
</template>

<script>
import router from "@/router";

export default {
  name: 'ExpItem',
  props: {
    title: String,
    id: Number
  },
  methods: {
    // deleteExp(event) {
    //   console.log('deleteExp', event)
    // },
    openExp(event) {
      router.push('/result/'+this.id)
      console.log('openExp', event)
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
