<script setup>
import Navbar from "@/components/Navbar.vue";
</script>

<template>
  <div>
    <h1>Filters</h1>
    <hr />
  </div>
  <Navbar />
  <router-view />
</template>

<style scoped>
h1 {
  margin: 0 0 1rem;
  text-align: center;
}
hr {
  margin: 0 0 1rem;
}
</style>
