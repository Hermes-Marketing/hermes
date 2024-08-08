<template>
  <div class="card" @click="goToCardView">
    <img :src="cardData.image" alt="Card Image" class="card-image" />
    <div class="card-details">
      <h3>{{ cardData.name }}</h3>
      <p>Owner: {{ cardData.owner }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    cardData: {
      type: Object,
      required: true,
    },
  },
  methods: {
    goToCardView() {
      this.$router.push({
        name: "CardView",
        params: { id: this.cardData.id },
      });
    },
  },
};
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  margin: 8px;
  cursor: pointer;
  transition: box-shadow 0.3s;
}
.card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.card-image {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 8px;
}
.card-details {
  margin-top: 12px;
}
</style>
