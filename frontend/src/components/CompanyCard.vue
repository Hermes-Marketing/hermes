<template>
  <div class="card">
    <h2>{{ company.business_name }}</h2>
    <p>{{ company.category }}</p>
    <p>{{ company.city }}, {{ company.state }}</p>
    <a :href="company.website" target="_blank">Visit Website</a>
  </div>
</template>

<script>
export default {
  props: {
    company: Object
  }
};
</script>

<style scoped>
.card {
  border: 1px solid #ddd;
  padding: 1rem;
  margin: 1rem;
}
</style>
