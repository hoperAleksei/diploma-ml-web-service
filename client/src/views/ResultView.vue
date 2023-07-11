<template>
  <!--  {{ res }}-->
<!--  <v-card v-for="rr in res">-->
<!--    <v-card-->
<!--        class="mx-auto ma-5 w-auto overflow-auto"-->
<!--        v-for="r in rr"-->
<!--        :title="r.alg_name"-->
<!--        max-width="800"-->
<!--    >-->
<!--    <table-res v-bind:alg="r" v-bind:metrics="metrics"></table-res>-->
<!--    </v-card>-->
<!--  </v-card>-->
  <res-list v-bind:list="res" v-bind:metrics="metrics"></res-list>

</template>

<script>
import store from "@/store";
import TableRes from "@/components/TableRes.vue";
import ResList from "@/components/ResList.vue";

export default {
  name: 'ResultView',
  components: {ResList, TableRes},
  props: {
    id: String
  },
  computed: {
  },
  data() {
    return {
      res: [],
      metrics: ['accuracy', 'error_rate', 'precision', 'recall', 'f1'],
    }
  },
  methods: {
    async updateRes() {
      this.res = await store.dispatch('getRes', {id: this.$props.id})
      console.log(this.res)
    }
  },
  async mounted() {
    console.log("m")
    await this.updateRes()
  }
}
</script>

<style scoped>

</style>
