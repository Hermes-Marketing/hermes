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
import Navbar from "@/components/Navbar.vue";
import { ref, provide } from "vue";

export default {
  name: "App",
  components: {
    Navbar,
  },
  setup() {
    const selected = ref({
      category: null,
      subCategory: null,
    });

    const handleCategorySelected = (newSelection) => {
      selected.value = newSelection;
    };

    const handleSubCategorySelected = (newSelection) => {
      selected.value = newSelection;
    };
    // Provide selected state to child components
    provide("selected", selected);

    return {
      selected,
      handleCategorySelected,
      handleSubCategorySelected,
    };
  },
};
</script>
