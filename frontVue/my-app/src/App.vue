<template>
  <div class="mytime">
    <MyTimepicker />
  </div>
</template>

<script>
import MyTimepicker from './components/MyTimepicker.vue';

export default {
  name: 'App',
  components: {
    MyTimepicker
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
