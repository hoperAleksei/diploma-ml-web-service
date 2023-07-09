<template>
  <v-card
      class="mx-auto w-auto"
      max-width="700"
  >
    <v-list>
      <exp-item
          v-for="item in items"
          :key="item.title"
          :title="item.title"
          :modelCount="item.modelCount"></exp-item>
    </v-list>
  </v-card>
</template>

<script>
import ExpItem from "@/components/ExpItem.vue";

export default {
  name: 'ExpList',
  components: {ExpItem},
  data() {
    return {
      items: [
        {
          title: 'Experiment 1',
          modelCount: 10,
        },
        {
          title: 'Experiment 2',
          modelCount: 11,
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
