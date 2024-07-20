<template>
  <div class="card" @click="goToWebsite">
    <img :src="business.image" alt="Business Image" class="card-image" />
    <div class="card-content">
      <h3>{{ business.name }}</h3>
      <p>Owner: {{ business.owner }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    business: {
      type: Object,
      required: true,
    },
  },
  methods: {
    goToWebsite() {
      if (this.business.website) {
        window.open(this.business.website, "_blank");
      }
    },
  },
};
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
  margin: 1rem;
  cursor: pointer;
  transition: box-shadow 0.3s;
}
.card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.card-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}
.card-content {
  padding: 1rem;
}
</style>
