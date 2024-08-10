<template>
  <div class="card-list">
    <Card v-for="card in filteredCards" :key="card.id" :cardData="card" />
  </div>
</template>

<script>
import Card from "@/components/Card.vue";

export default {
  name: "CardList",
  components: {
    Card,
  },
  props: {
    cards: {
      type: Array,
      required: true,
    },
    selected: {
      type: Object,
      required: true,
    },
  },
  computed: {
    filteredCards() {
      if (!this.selected) {
        console.log("Selected is not defined");
        return this.cards;
      }
      console.log("Filtering cards with:", this.selected);
      return this.cards.filter((card) => {
        return (
          (!this.selected.category ||
            card.category === this.selected.category) &&
          (!this.selected.subCategory ||
            card.subCategory === this.selected.subCategory)
        );
      });
    },
  },
};
</script>

<style scoped>
.card-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
