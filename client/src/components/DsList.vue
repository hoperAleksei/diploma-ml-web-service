<template>
  <v-card
      class="mx-auto w-auto"
      max-width="700"
  >
    <v-btn icon="mdi-reload" @click="getDatasets" class="ma-1"></v-btn>
<!--    <v-btn @click="getDatasets" class="ma-1">-->
<!--      Обновить-->
<!--    </v-btn>-->
    <v-list>
      <ds-item
          v-for="item in items"
          :id="item.id"
          :title="item.name"></ds-item>
    </v-list>
  </v-card>
</template>

<script>
import DsItem from "@/components/DsItem.vue";
import {getState} from "@/api/experiment";
import store from "@/store";

export default {
  name: 'DsList',
  components: {DsItem},
  computed: {},
  data() {
    return {
      items: []
    }
  },
  methods: {
    async getDatasets() {
      this.items = []
      let res = {}
      try {
        res = await store.dispatch('getDatasets')
      } catch (e) {
        console.log(e)
      }
      this.items = res
    }
  },
  mounted() {
    this.getDatasets()
  }
}
</script>

<style lang="scss" scoped>

</style>
