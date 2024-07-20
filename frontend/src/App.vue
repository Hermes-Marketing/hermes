<template>
  <div id="app">
    <Navbar @category-selected="fetchData" />
    <CardList :selectedData="selectedData" />
  </div>
</template>

<script setup>
import { ref } from "vue";
import Navbar from "./components/Navbar.vue";
import CardList from "./components/CardList.vue";

const selectedData = ref({ category: "", subCategory: "" });

const fetchData = (data) => {
  selectedData.value = data;
};
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.navbar {
  position: sticky;
  top: 0;
  width: 100%;
  background-color: #333;
  z-index: 1000;
}

.card-list {
  margin-top: 1rem;
  width: 100%;
}
</style>
