<template>
  <v-table class="overflow-auto">
    <thead>
    <tr>
      <th v-for="name in dataset.names" :key="name"> {{ name }}</th>
    </tr>
    <tr>
      <th v-for="type in dataset.types" :key="type"> {{ type }}</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="line in dataset.lines" :>

    </tr>
    </tbody>
  </v-table>
</template>

<script>
export default {
  name: 'TableDs',
  data() {
    return {
      dataset: {
        names: ['name 1', 'name 2', 'name 3', 'name 4', 'name 5', 'name 6'],
        types: ['float64', 'object', 'int32', 'int32', 'int32', 'int32'],
        lines: [
          [2.2, 'var 1', 1, 1, 1, 1],
          [2.1, 'var 2', 2, 1, 1, 1],
          [3.4, 'var 1', 3, 1, 1, 1],
          [5.6, 'var 2', 2, 1, 1, 1],
          [7.2, 'var 1', 2, 1, 1, 1],
          [0.3, 'var 2', 2, 1, 1, 1],
        ]
      }
    }
  }
}
</script>

<style scoped>

</style>
