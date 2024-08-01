<template>
  <nav v-if="subCategories && subCategories.length" class="sub-navbar">
    <div class="navbar-menu">
      <div class="navbar-start">
        <router-link
          v-for="subCat in subCategories"
          :key="subCat"
          to="/"
          class="navbar-item"
          @click="selectSubCategory(subCat)"
        >
          {{ subCat }}
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "SubNavbar",
  props: {
    subCategories: {
      type: Array,
      required: true,
    },
  },
  methods: {
    selectSubCategory(subCategory) {
      this.$emit("subCategorySelected", subCategory);
    },
  },
};
</script>

<style scoped>
.sub-navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #444;
  color: #fff;
}
.navbar-item {
  color: #fff;
  text-decoration: none;
  margin: 0 2rem;
}
.navbar-item:hover {
  text-decoration: underline;
}
</style>
