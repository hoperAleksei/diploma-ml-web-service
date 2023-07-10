<template>
  <pre-sel></pre-sel>
  <table-ds ref="table"></table-ds>
  <v-btn @click="commit">Перейти к разбиению</v-btn>
</template>

<script>
import TableDs from "@/components/TableDs.vue";
import PreSel from "@/components/PreSel.vue";
import store from "@/store";
import router from "@/router";

export default {
  name: 'PreproView',
  components: {PreSel, TableDs},
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
