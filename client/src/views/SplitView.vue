<template>
  <v-card
      class="mx-auto w-auto"
      max-width="700"
  >
    <v-form @submit.prevent="submit" class="pa-3">
      <!--      {{splits}}-->
      <v-btn icon="mdi-plus"
             @click="addSplit"
             v-if="splits.length < 3"
             class="pa-1"
      ></v-btn>
      <v-btn icon="mdi-minus"
             @click="dropSplit"
             v-if="splits.length > 1"
             class="ma-1"
      ></v-btn>
      <v-spacer></v-spacer>
      <v-btn type="submit" class="flot-right ma-3">Применить разбиения</v-btn>

      <v-card v-for="(split, i) in splits" class="overflow-visible pa-2 ma-2">
        <v-card class="d-flex overflow-visible pa-2 ma-2 align-center ma-1">
          <v-label>
            Размер тестовой выборки
          </v-label>
          <v-slider v-model="split.ts"
                    :min="1"
                    :max="99"
                    :step="1"
                    thumb-label
                    style="max-width: 150px"
                    hide-details
                    class="overflow-visible"
          ></v-slider>
          <v-text-field
              v-model="split.ts"
              hide-details
              single-line
              density="compact"
              type="number"
              style="max-width: 70px"
              class="align-center"
              variant="outlined"
          ></v-text-field>
        </v-card>
        <v-card class="d-flex overflow-visible pa-2 align-center ma-1">
          <v-label class="pr-3">
            Коэффициент случайности
          </v-label>
          <v-text-field v-model="split.rs"
                        style="max-width: 70px"
                        type="number"
                        hide-details
                        variant="outlined"
          ></v-text-field>
          <v-switch
              label="Стратификация"
              v-model="split.st"
              hide-details
              class="px-5"
          ></v-switch>
        </v-card>
      </v-card>
    </v-form>
  </v-card>
</template>

<script>
import store from "@/store";
import router from "@/router";

export default {
  name: 'SplitView',
  data() {
    return {
      splits: [
        {
          ts: 20,
          rs: 0,
          st: false,
        }
      ],
      loading: false,
    }
  },
  methods: {
    addSplit() {
      this.splits.push(
          {
            ts: 20,
            rs: 0,
            st: false,
          }
      )
    },
    dropSplit(event) {
      if (this.splits.length > 1) {
        this.splits.pop()
      }
    },
    async submit() {
      this.loading = true
      let req = []
      for (let ri in this.splits) {
        const r = this.splits[ri]
        req.push(
            {
              ts: r.ts,
              rs: Number(r.rs),
              st: r.st ? "yes" : "no",
            }
        )
      }
      const res = await store.dispatch("postSplits", {splits: req})
      if (res.status) {
        await store.dispatch("updateState")
        router.push("/autofit")
      } else {
        console.log("error")
      }
      this.loading = false


    }
  }
}
</script>

<style lang="scss" scoped>

</style>
