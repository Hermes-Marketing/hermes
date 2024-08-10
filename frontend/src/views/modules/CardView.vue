<template>
  <div v-if="cardData" class="card-view">
    <img :src="cardData.image" alt="Card Image" class="card-view-image" />
    <div class="card-view-details">
      <h1>{{ cardData.name }}</h1>
      <p>Owner: {{ cardData.owner }}</p>
      <p>Category: {{ cardData.category }}</p>
      <p>SubCategory: {{ cardData.subCategory }}</p>
      <!-- Updated link to open in a new tab -->
      <a
        :href="cardData.website"
        target="_blank"
        rel="noopener noreferrer"
        class="website-link"
        >Visit Website</a
      >
    </div>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
import { useRoute } from "vue-router";
import { inject, computed } from "vue";

export default {
  setup() {
    const route = useRoute();
    const cards = inject("cards", []);
    const cardId = route.params.id;

    const cardData = computed(() => {
      return cards.value.find((card) => card.id === parseInt(cardId));
    });

    return {
      cardData,
    };
  },
};
</script>

<style scoped>
.card-view {
  padding: 20px;
}
.card-view-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 8px;
}
.card-view-details {
  margin-top: 20px;
}
.website-link {
  display: inline-block;
  margin-top: 10px;
  padding: 10px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}
.website-link:hover {
  background-color: #0056b3;
}
</style>
