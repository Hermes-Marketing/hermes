<template>
  <div id="home">
    <CardList :cards="filteredCards" :selected="selected" />
  </div>
</template>

<script>
import { computed, inject, reactive } from "vue";
import CardList from "@/views/modules/CardList.vue";

export default {
  name: "Home",
  components: {
    CardList,
  },
  setup() {
    const selected = inject("selected", () =>
      reactive({ category: null, subCategory: null })
    );

    const cards = inject("cards", () => ref([]));

    const filteredCards = computed(() => {
      if (!cards.value.length || !selected.value) {
        console.log("Cards are empty or selected is undefined.");
        return cards.value;
      }

      return cards.value.filter((card) => {
        const categoryMatch =
          !selected.value.category || card.category === selected.value.category;
        const subCategoryMatch =
          !selected.value.subCategory ||
          card.subCategory === selected.value.subCategory;
        return categoryMatch && subCategoryMatch;
      });
    });

    return {
      filteredCards,
      selected,
    };
  },
};
</script>

<style scoped>
/* Add any styles needed for Home.vue */
</style>
