<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <a class="navbar-item" href="#"> MyBrand </a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item" href="#home">Home</a>
        <a class="navbar-item" href="#about">About</a>
        <a class="navbar-item" href="#contact">Contact</a>
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
