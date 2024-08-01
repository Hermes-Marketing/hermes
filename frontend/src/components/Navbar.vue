<template>
  <div>
    <nav class="navbar" ref="navbar">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item" @click.prevent="resetSelection"
          >Hermes</router-link
        >
        <router-link to="/admin" class="navbar-item">
          <i class="fas fa-user-shield"></i> Admin
        </router-link>
      </div>
      <div class="navbar-menu">
        <div class="navbar-start">
          <router-link
            to="/"
            class="navbar-item"
            @click.prevent="selectCategory('Bar')"
          >
            <i class="fas fa-cocktail"></i> Bar
          </router-link>
          <router-link
            to="/"
            class="navbar-item"
            @click.prevent="selectCategory('Construction')"
          >
            <i class="fas fa-hard-hat"></i> Construction
          </router-link>
          <router-link
            to="/"
            class="navbar-item"
            @click.prevent="selectCategory('Food')"
          >
            <i class="fas fa-utensils"></i> Food
          </router-link>
          <router-link
            to="/"
            class="navbar-item"
            @click.prevent="selectCategory('Legal')"
          >
            <i class="fas fa-balance-scale"></i> Legal
          </router-link>
          <router-link
            to="/"
            class="navbar-item"
            @click.prevent="selectCategory('Restaurant')"
          >
            <i class="fas fa-utensil-spoon"></i> Restaurant
          </router-link>
          <router-link
            to="/"
            class="navbar-item"
            @click.prevent="selectCategory('Wine')"
          >
            <i class="fas fa-wine-bottle"></i> Wine
          </router-link>
        </div>
      </div>
    </nav>
    <SubNavbar
      v-if="showSubNavbar"
      ref="subNavbar"
      :subCategories="subCategories[selected.category]"
      @subCategorySelected="handleSubCategorySelected"
    />
  </div>
</template>

<script>
import SubNavbar from "@/components/SubNavbar.vue";

export default {
  name: "Navbar",
  components: {
    SubNavbar,
  },
  data() {
    return {
      selected: {
        category: null,
        subCategory: null,
      },
      showSubNavbar: false,
      subCategories: {
        Bar: [
          "Tap and Social",
          "Lounge",
          "Pub",
          "Barcade",
          "Tavern",
          "Sports bar",
          "Bar and Grill",
          "Taproom",
          "Brewery",
        ],
        Construction: [
          "Roofing",
          "Residential Homes",
          "Services",
          "Contracting",
        ],
        Food: ["Catering", "Butcher & Grocer"],
        Legal: ["Attorney", "Estate", "Litigation"],
        Restaurant: [
          "Sandwiches",
          "Steak house",
          "Steak",
          "Diner",
          "Family",
          "Fine Dining",
          "Italian",
          "Modern Cuisine",
        ],
        Wine: ["Winery", "Wine and Spirits", "Vineyards"],
      },
    };
  },
  methods: {
    selectCategory(category) {
      this.selected.category = category;
      this.selected.subCategory = null;
      this.showSubNavbar = true;
      console.log(this.selected);
    },
    handleSubCategorySelected(subCategory) {
      this.selected.subCategory = subCategory;
      this.showSubNavbar = false;
      console.log(this.selected);
    },
    resetSelection() {
      this.selected.category = null;
      this.selected.subCategory = null;
      this.showSubNavbar = false;
      console.log(this.selected);
    },
    handleClickOutside(event) {
      const navbar = this.$refs.navbar;
      const subNavbar = this.$refs.subNavbar ? this.$refs.subNavbar.$el : null;
      if (
        navbar &&
        !navbar.contains(event.target) &&
        subNavbar &&
        !subNavbar.contains(event.target)
      ) {
        this.showSubNavbar = false;
        console.log(this.selected);
      }
    },
  },
  mounted() {
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeDestroy() {
    document.removeEventListener("click", this.handleClickOutside);
  },
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #333;
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
