<template>
  <v-card
      class="mx-auto w-auto overflow-auto"
      max-width="800"
  >
    <v-table
        fixed-header
        height="500">
      <thead>
      <tr>
        <th v-for="name in dataset.names">{{ name }}</th>
      </tr>
      <tr>
        <th v-for="type in dataset.types">{{ type }}</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="line in dataset.lines">
        <td v-for="el in line">{{ el }}</td>
      </tr>
      </tbody>
    </v-table>
  </v-card>
</template>

<script>
import store from "@/store";

export default {
  name: 'TableDs',

  data() {
    return {
      dataset: {}
    }
  },
  methods: {
    async update() {
      const res = await store.dispatch('getTable')
      if (res.status) {
        this.dataset = res.table
      } else {
        console.log('error')
      }
    }
  },
  mounted() {
    this.update()
  }
}
</script>

<style scoped>

</style>
