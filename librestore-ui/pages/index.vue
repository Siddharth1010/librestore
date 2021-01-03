<template>
  <div>
    <Product title="Carrots" price="3.99"></Product>
    <Product title="Beans" price="1.50"></Product>
    <Product title="Bacon" price="9.00"></Product>
    <Product title="Rice" price="5.99"></Product>
  </div>
</template>

<script>
import Product from '~/components/Product.vue'

export default {
  components: {
    Product,
  },
}
</script>
<style scoped>
div {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
