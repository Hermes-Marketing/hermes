<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">Hermes</router-link>
    </div>
    <div class="navbar-menu">
      <div class="navbar-start">
        <router-link to="/admin" class="navbar-item">
          <i class="fas fa-user-shield"></i> Admin
        </router-link>
        <router-link to="/" class="navbar-item">
          <i class="fas fa-cocktail"></i> Bar
        </router-link>
        <router-link to="/" class="navbar-item">
          <i class="fas fa-hard-hat"></i> Construction
        </router-link>
        <router-link to="/" class="navbar-item">
          <i class="fas fa-utensils"></i> Food
        </router-link>
        <router-link to="/" class="navbar-item">
          <i class="fas fa-balance-scale"></i> Legal
        </router-link>
        <router-link to="/" class="navbar-item">
          <i class="fas fa-utensil-spoon"></i> Restaurant
        </router-link>
        <router-link to="/" class="navbar-item">
          <i class="fas fa-wine-bottle"></i> Wine
        </router-link>
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
