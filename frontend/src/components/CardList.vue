<template>
  <div class="card-list">
    <Card
      v-for="business in filteredBusinesses"
      :key="business.id"
      :business="business"
    />
  </div>
</template>

<script>
import Card from "./Card.vue";

export default {
  name: "CardList",
  components: {
    Card,
  },
  props: {
    selectedData: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      businesses: [], // This will hold the data fetched from the API
    };
  },
  watch: {
    //This watches for any change in selected categories
    selectedData: {
      immediate: true,
      handler(newData) {
        this.fetchData(newData);
      },
    },
  },
  computed: {
    filteredBusinesses() {
      if (!this.selectedData.category && !this.selectedData.subCategory) {
        return this.businesses;
      }
      return this.businesses.filter(
        (business) =>
          business.category === this.selectedData.category &&
          business.subCategory === this.selectedData.subCategory
      );
    },
  },
  methods: {
    async fetchData(selectedData) {
      // Placeholder for API call - replace with actual API call
      const response = await this.mockApiCall();
      this.businesses = response;
    },
    async mockApiCall() {
      // Placeholder data
      return [
        {
          id: 1,
          name: "Tap and Social Business",
          owner: "Owner 1",
          image: "https://via.placeholder.com/300",
          website: "https://example.com",
          category: "Bar",
          subCategory: "Tap and Social",
        },
        {
          id: 2,
          name: "Italian Restaurant",
          owner: "Owner 2",
          image: "https://via.placeholder.com/300",
          website: "https://example.com",
          category: "Restaurant",
          subCategory: "Italian",
        },
      ];
    },
  },
};
</script>

<style scoped>
.card-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 1rem;
  width: 100%;
}
</style>
