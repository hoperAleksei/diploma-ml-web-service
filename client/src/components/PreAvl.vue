<template>
  <v-card>
    <v-card v-for="alg in algs"
            :color="alg.color"
            class="pa-1 ma-1"
    >{{ alg.name }}
    </v-card>
  </v-card>
</template>

<script>
import store from "@/store";

export default {
  name: 'PreAvl',
  data() {
    return {
      algs: []
    }
  },
  methods: {
    async upgrade() {
      this.algs = []
      const res = await store.dispatch('getAvailable')
      for (let i in res) {
        const r = res[i]
        console.log((r.status === 'ok') ? 'red' : 'green')

        this.algs.push({
          name: r.name,
          color: (r.status === 'ok') ? 'green' : 'red'
        })
      }
    }
  },
  mounted() {
    this.upgrade()
  }
}
</script>

<style scoped>

</style>
