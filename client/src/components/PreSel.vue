<template>
  <v-form ref="form" @submit.prevent="submit">
    <v-card max-width="600" class="d-flex flex-row flex-wrap mx-auto">

      <!--      <v-container>-->
      <v-select v-model="values[i]"
                clearable
                v-for="(pre, i) in preSl"
                :label="pre.name"
                :hint="pre.desc"
                persistent-hint
                :items="pre.methods"
                item-title="name"
                item-value="nm"
                class="pa-3"
      ></v-select>

      <v-select v-model="valuesMu[i]"
                multiple
                chips
                v-for="(pre, i) in preMu"
                :label="pre.name"
                :hint="pre.desc"
                persistent-hint
                :items="pre.value"
                item-title=""
                item-name=""
                class="pa-3"
      ></v-select>
      <!--      <v-card class="d-flex"-->
      <!--              v-for="(pre, i) in preMuMa">-->
      <!--        {{ i}}-->
      <!--        <v-select-->
      <!--            v-model="valuesMuMa[i][0]"-->
      <!--            class="pa-1"-->
      <!--        ></v-select>-->
      <!--        <v-select-->
      <!--            label="Количество"-->
      <!--            v-model="valuesMuMa[i][1]"-->
      <!--            class="pa-1"-->
      <!--        ></v-select>-->
      <!--      </v-card>-->
      <!--      </v-container>-->
      <v-container class="d-flex justify-space-around">
        <v-btn type="submit">Применить</v-btn>
        <v-btn @click="reset">Сбросить</v-btn>
      </v-container>
    </v-card>
  </v-form>
</template>

<script>
import store from "@/store";
import {isProxy, toRaw} from 'vue'

export default {
  name: 'PreSel',
  computed: {
    preSl() {
      let res = []
      res.push({
        type: "label",
        name: "Название признака для классификации",
        desc: "Признак будет использован для классификации",
        methods: [...toRaw(this.names)]
      })
      for (let mth in this.pres) {
        if (this.pres[mth].methods) {
          res.push(this.pres[mth])
        }
      }
      return res
    },
    preMu() {
      let res = []
      for (let mth in this.pres) {
        if ((this.pres[mth].value) && !(this.pres[mth].methods)) {
          let rr = this.pres[mth]
          switch (this.pres[mth].value) {
            case 'Лист признаков':
              rr.value = [...toRaw(this.names)]
              break
            case 'Лист значений':
              rr.value = ["-", "?", "Null", "None", "NaN"]
              break
          }
          res.push(rr)
        }
      }
      return res
    },
    preMuMa() {
      let res = []
      for (let mth in this.pres) {
        if ((this.pres[mth].value) && (this.pres[mth].methods)) {
          let rr = this.pres[mth]
          switch (this.pres[mth].value) {
            case 'Число':
              rr.value = []
              for (let i in this.names) {
                rr.value.push(i)
              }
              break
          }
          res.push(rr)
        }
      }
      return res
    },
  },
  data() {
    return {
      names: [],
      pres: [],
      values: [],
      valuesMu: [],
      valuesMuMa: [],
      label: ''
    }
  },
  methods: {
    async submit() {
      let req = {}
      for (let i in this.values) {
        const type = this.preSl[i].type
        const mth = this.values[i]
        req[type] = mth
      }
      for (let i in this.valuesMu) {
        const type = this.preMu[i].type
        const mth = toRaw(this.valuesMu[i])
        req[type] = mth
      }

      const res = await store.dispatch("prepro", {req: req})
      if (res.status) {
        console.log(this.$parent.$parent.$refs.table.$refs)
        await this.$parent.$parent.$refs.table.update()
        this.values = []
        this.valuesMu = []
        this.valuesMuMa = []
        await this.updateNames()
        await this.updatePres()
      } else {
        console.log("error")
      }
    },
    async updatePres() {
      this.pres = await store.dispatch("getPre")
    },
    async updateNames() {
      this.names = await store.dispatch("getDsNames")
    },
    async reset() {
      this.values = []
      this.valuesMu = []
      this.valuesMuMa = []
      await store.dispatch("restoreDs")
      await this.$parent.$refs.table.update()
      await this.updateNames()
      await this.updatePres()
    }
  },
  mounted() {
    this.updateNames()
    this.updatePres()
  }
}
</script>

<style>
iframe#webpack-dev-server-client-overlay {
  display: none !important;
}

.v-select {
  max-width: 300px;
}
</style>
