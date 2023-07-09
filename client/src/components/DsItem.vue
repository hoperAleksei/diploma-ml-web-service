<template>
  <v-list-item :key="$props.id" @click="selectDs">
<!--    <div>-->
      <v-list-item-title>{{ $props.title }}</v-list-item-title>
<!--    </div>-->
  </v-list-item>
</template>

<script>
import store from "@/store";
import router from "@/router";

export default {
  name: 'ExpItem',
  props: {
    id: Number,
    title: String,
  },
  methods: {
    async selectDs(event) {
      const res = await store.dispatch('useDataset', {id: this.id})
      if (res) {
        router.push('/preprocess')
      }
      else {
        console.log(2)
      }
    }
  }
}
</script>

<style scoped>

</style>
