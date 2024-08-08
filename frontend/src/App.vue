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

    const cards = ref([]);

    const fetchCards = async () => {
      try {
        const response = await fetch("http://localhost:8000/v1/company/"); // Adjust URL as needed
        if (response.ok) {
          const data = await response.json();
          cards.value = data;
        } else {
          console.error("Failed to fetch cards:", response.status);
        }
      } catch (error) {
        console.error("Error fetching cards:", error);
      }
    };

    onMounted(fetchCards);

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
