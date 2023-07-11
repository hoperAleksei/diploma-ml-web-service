<template>
  <v-card
      class="mx-auto w-auto"
      max-width="700"
  >
<!--    {{items}}-->
    <v-list>
      <exp-item
          v-for="item in items"
          :id="item.id"
          :title="item.name"></exp-item>
    </v-list>
  </v-card>
</template>

<script>
import ExpItem from "@/components/ExpItem.vue";
import store from "@/store";

export default {
  name: 'ExpList',
  components: {ExpItem},
  data() {
    return {
      items: [
      ]
    }
  },
  methods: {
    async update() {
      const res = await store.dispatch('getExps')
      this.items = res
    }
  },
  async mounted() {
    await this.update()
  }
}
</script>

<style lang="scss" scoped>

</style>
