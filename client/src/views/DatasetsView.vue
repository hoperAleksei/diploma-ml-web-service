<template>
  <div>
  <ds-add></ds-add>
  <ds-list ref="list"></ds-list>
  </div>
</template>

<script>
import DsAdd from "@/components/DsAdd.vue";
import DsList from "@/components/DsList.vue";

export default {
  name: 'DatasetsView',
  components: {DsList, DsAdd},
  data: () => ({

  }),
  methods: {

  }
}
</script>

<style lang="scss" scoped>

</style>
