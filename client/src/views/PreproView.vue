<template>
  <v-card class="d-flex pa-5">
    <v-card class="w-50 d-flex flex-column">
      <pre-sel></pre-sel>
      <v-btn @click="commit" color="green" class="mt-2 align-self-center">Перейти к разбиению</v-btn>
    </v-card>
    <v-card class="w-50">
      <pre-avl class="w-10 align-self-center"></pre-avl>
      <table-ds ref="table" class="w-1"></table-ds>
    </v-card>
  </v-card>
</template>

<script>
import TableDs from "@/components/TableDs.vue";
import PreSel from "@/components/PreSel.vue";
import store from "@/store";
import router from "@/router";
import PreAvl from "@/components/PreAvl.vue";

export default {
  name: 'PreproView',
  components: {PreAvl, PreSel, TableDs},
  data: () => ({}),
  methods: {
    async commit() {
      const res = await store.dispatch('preCommit')
      if (res.status) {
        await store.dispatch("updateState")
        router.push('/split')
      } else {
        console.log('error')
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
