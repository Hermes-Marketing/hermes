<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <a class="navbar-item" href="#"> MyBrand </a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item" href="#bar"
          ><i class="fas fa-cocktail"></i> Bar</a
        >
        <a class="navbar-item" href="#construction"
          ><i class="fas fa-hard-hat"></i> Construction</a
        >
        <a class="navbar-item" href="#food"
          ><i class="fas fa-utensils"></i> Food</a
        >
        <a class="navbar-item" href="#legal"
          ><i class="fas fa-balance-scale"></i> Legal</a
        >
        <a class="navbar-item" href="#restaurant"
          ><i class="fas fa-utensil-spoon"></i> Restaurant</a
        >
        <a class="navbar-item" href="#wine"
          ><i class="fas fa-wine-bottle"></i> Wine</a
        >
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #333;
  color: #fff;
}

.navbar-item {
  color: #fff;
  text-decoration: none;
  margin: 0 0.5rem;
}

.navbar-item:hover {
  text-decoration: underline;
}
</style>
