<template>
  <div id="app">
    <nav>
      <router-link to="/">Companies</router-link>
      <router-link to="/plan-route">Plan Route</router-link>
    </nav>
    <div id="app-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
/* Sigma Chi Themed Colors */
:root {
  --primary-blue: #0033A0; /* Sigma Chi blue */
  --primary-gold: #FFD700; /* Sigma Chi gold */
  --background-color: #F0F2F5; /* Soft background */
  --font-color: #333; /* Text color */
  --font-family: 'Roboto', sans-serif; /* Clean, modern font */
}

/* Global Styles */
html, body, #app {
  height: 100%;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--font-family);
  background-color: var(--background-color);
  color: var(--font-color);
}

/* Navigation Styling */
nav {
  background-color: var(--primary-blue);
  padding: 1rem;
  display: flex;
  justify-content: space-around;
  color: white;
}

nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}

/* Ensures app content takes full height */
#app {
  display: flex;
  flex-direction: column;
}

#app-content {
  flex: 1;
  padding: 2rem; /* Add some padding for a nicer layout */
}
</style>
