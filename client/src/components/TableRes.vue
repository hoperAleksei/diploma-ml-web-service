<template>
  <v-table
          fixed-header
          height="500">
        <thead>
        <tr>
          <th v-for="par in alg.hyperparams_names">{{ par }}</th>
          <th v-for="mtr in metrics">{{ mtr }}</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="line in alg.experiment">
          <td v-for="par in alg.hyperparams_names">{{ line.hyperparams[par] }}</td>
          <td v-for="mtr in metrics">{{ line.metrics[mtr] }}</td>
        </tr>
        </tbody>
      </v-table>
</template>

<script>
export default {
  name: "TableRes",
  props: {
    alg: Object,
    metrics: Array,

  }
}
</script>

<style scoped>

</style>
