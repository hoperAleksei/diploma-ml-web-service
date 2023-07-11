<template>
  <v-form @submit.prevent="submit" class="pa-2 ma-2">
    <v-card v-for="(alg, i) in algs" class="d-flex overflow-visible ma-2 pa-2">
      <v-card :title="alg.name" class="d-flex flex-column  flex-1-1 w-70 overflow-visible">
        <v-card v-for="(param, j) in alg.params" class="d-flex flex-column overflow-visible">
          <v-range-slider v-if="param.type !== 'set'"
                          v-model="res[i].params[j].value"
                          :label="param.name"
                          :min="param.min"
                          :max="param.max"
                          :step="1"
                          thumb-label
                          hide-details
                          class="overflow-visible ma-2 pa-2"
          >
            <template v-slot:prepend>
              <v-text-field
                  v-model="res[i].params[j].value[0]"
                  hide-details
                  single-line
                  type="number"
                  variant="outlined"
                  density="compact"
                  style="width: 70px"
                  @change="$set(range, 0, $event)"
              ></v-text-field>
            </template>
            <template v-slot:append>
              <v-text-field
                  v-model="res[i].params[j].value[1]"
                  hide-details
                  single-line
                  type="number"
                  variant="outlined"
                  style="width: 70px"
                  density="compact"
              ></v-text-field>
            </template>
          </v-range-slider>
          <v-select
              v-model="res[i].params[j].value"
              class="ma-2 pa-2"
              v-if="param.type === 'set'"
              :items="param.values"
              :label="param.name"
              chips
              multiple
          ></v-select>
        </v-card>
      </v-card>
      <v-card :text="alg.desc" class="pa-2 ma-2 " style="max-width: 400px">

      </v-card>
    </v-card>
    <v-btn type="submit" color="orange">Провести эксперимент</v-btn>
  </v-form>
</template>

<script>
import store from "@/store";
import router from "@/router";

export default {
  name: 'AutofitView',
  data() {
    return {
      algs: [],
      res: [],
      loading: false,
    }
  },
  methods: {
    async submit() {
      this.loading = true

      let req = []
      for (let i in this.res) {
        const alg = this.algs[i]
        const par = this.res[i].params
        let pr = []
        for (let j in par) {
          const p = par[j]
          if (alg.params[j].type !== 'set') {

            pr.push({
              name: p.name,
              type: alg.params[j].type,
              min: p.value[0],
              max: p.value[1],
            })
          } else {
            console.log("loxsosi", p.value)
            pr.push({
              name: p.name,
              type: alg.params[j].type,
              values: p.value,
            })
          }
        }
        req.push({
          alg_name: alg.name,
          n_steps: 3,
          params: pr
        })
      }
      console.log(req)

      const res = await store.dispatch('runExp', {algs: req})

      if (res) {
        await store.dispatch('updateState')
        router.push('/')
      }
      else {
        console.log("error")
      }

      this.loading = false
    },
    async load() {
      this.algs = await store.dispatch('getToRun')
      this.res = []
      for (let i in this.algs) {
        const a = this.algs[i]
        let p = []
        for (let j in a.params) {
          let pp = a.params[j]
          if (pp.type === 'set') {
                        p.push({
              name: pp.name,
              value: [...pp.values]
            })
          }
          else {

            p.push({
              name: pp.name,
              value: [pp.min, pp.max]
            })
          }
        }
        this.res.push({
          name: a.name,
          params: p
        })
      }
    }
  },
  async mounted() {
    await this.load()
  }
}
</script>

<style scoped>

</style>
