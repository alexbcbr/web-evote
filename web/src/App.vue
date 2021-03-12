<template>
  <div id="app">
    <Candidate msg="Eleições Presidenciais 2021"/>
  </div>
</template>

<script>
import Candidate from './components/Candidate.vue'

export default {
  name: 'App',
  components: {
    Candidate
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
