<template>

  <!--  {{name}}-->
  <!--  :title="list[0].name"-->
  <!--            :title="list[0].split"-->
  <!--  -->
  <v-card v-if="list[0]" :title="'Эксперимент: '+list[0].name" class="pa-5 ma-1">
    <v-card v-for="rr in list"
            class="mx-auto ma-5 w-auto overflow-auto"
            max-width="850">
      <v-card-title>Контроль:{{rr.split.ts}}, Коэффициент случайности: {{rr.split.ts}}{{rr.split.st ? ', Стратификация' : '.'}} </v-card-title>
      <v-card
          class="mx-auto ma-5 w-auto overflow-auto"
          v-for="r in rr.exps"
          :title="r.alg_name"
          max-width="800"
      >
        <table-res v-bind:alg="r" v-bind:metrics="metrics"></table-res>
      </v-card>
    </v-card>
  </v-card>
</template>

<script>
import TableRes from "@/components/TableRes.vue";

export default {
  name: "ResList",
  components: {TableRes},
  props: {
    list: Array,
    metrics: Array,
    name: String,
  },

}
</script>

<style scoped>

</style>
