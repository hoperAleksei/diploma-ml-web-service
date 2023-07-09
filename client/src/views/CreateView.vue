<template>
  <exp-add></exp-add>
  <exp-list></exp-list>
</template>

<script>

import {defineComponent} from "vue";
import ExpList from "@/components/ExpList.vue";
import ExpAdd from "@/components/ExpAdd.vue";

export default defineComponent({
  components: {ExpAdd, ExpList}
})
</script>

<style>

</style>
