<template>
  <div>
    <Navbar
      @categorySelected="handleCategorySelected"
      @subCategorySelected="handleSubCategorySelected"
    />
    <router-view :selected="selected" />
  </div>
</template>

<script>
import { ref, provide, reactive, onMounted } from "vue";
import Navbar from "@/components/Navbar.vue";
import { fetchAllCards } from "./services/fetchAllCards";

export default {
  name: "App",
  components: {
    Navbar,
  },
  setup() {
    const selected = reactive({
      category: null,
      subCategory: null,
    });

    const cards = ref([
      {
        id: 1,
        image: "https://via.placeholder.com/150",
        name: "The Social Tap",
        owner: "John Doe",
        category: "Bar",
        subCategory: "Tap and Social",
        website: "http://example.com",
      },
      {
        id: 2,
        image: "https://via.placeholder.com/150",
        name: "Lounge Life",
        owner: "Jane Smith",
        category: "Bar",
        subCategory: "Lounge",
        website: "http://example.com",
      },
      {
        id: 3,
        image: "https://via.placeholder.com/150",
        name: "The Urban Pub",
        owner: "Michael Brown",
        category: "Bar",
        subCategory: "Pub",
        website: "http://example.com",
      },
      {
        id: 4,
        image: "https://via.placeholder.com/150",
        name: "Modern Roofing",
        owner: "Lisa White",
        category: "Construction",
        subCategory: "Roofing",
        website: "http://example.com",
      },
      {
        id: 5,
        image: "https://via.placeholder.com/150",
        name: "Green Homes",
        owner: "Tom Green",
        category: "Construction",
        subCategory: "Residential Homes",
        website: "http://example.com",
      },
      {
        id: 6,
        image: "https://via.placeholder.com/150",
        name: "Gourmet Catering",
        owner: "Emily Johnson",
        category: "Food",
        subCategory: "Catering",
        website: "http://example.com",
      },
      {
        id: 7,
        image: "https://via.placeholder.com/150",
        name: "Fresh Butcher",
        owner: "David Lee",
        category: "Food",
        subCategory: "Butcher & Grocer",
        website: "http://example.com",
      },
      {
        id: 8,
        image: "https://via.placeholder.com/150",
        name: "Legal Aid Services",
        owner: "Sandra Kim",
        category: "Legal",
        subCategory: "Attorney",
        website: "http://example.com",
      },
      {
        id: 9,
        image: "https://via.placeholder.com/150",
        name: "The Family Diner",
        owner: "Robert Carter",
        category: "Restaurant",
        subCategory: "Family",
        website: "http://example.com",
      },
      {
        id: 10,
        image: "https://via.placeholder.com/150",
        name: "Vineyard Estates",
        owner: "Angela Davis",
        category: "Wine",
        subCategory: "Vineyards",
        website: "http://example.com",
      },
    ]);

    onMounted(fetchAllCards);

    provide("selected", selected);
    provide("cards", cards); // Providing cards at the app level

    const handleCategorySelected = (newSelection) => {
      selected.value = newSelection;
    };

    const handleSubCategorySelected = (newSelection) => {
      selected.value = newSelection;
    };

    return {
      selected,
      handleCategorySelected,
      handleSubCategorySelected,
    };
  },
};
</script>
