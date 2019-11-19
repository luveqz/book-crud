<template>
  <div class="container">
    <Navbar />
    <nuxt />
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'

export default {
  components: {
    Navbar
  }
}
</script>

<style lang="css">
  * {
    font-family: 'Open Sans';
    color: #334848;
    font-size: 14px
  }
  body {
    background-color: #e9eaea;
    padding: 0px;
    margin: 0px;
    top: 0px;
    left: 0px;
  }
</style>
