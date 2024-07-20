<template>
  <div>
    <nav class="navbar">
      <div class="navbar-brand">
        <a class="navbar-item" href="#"> MyBrand </a>
      </div>
      <div class="navbar-menu">
        <div class="navbar-start">
          <a
            v-for="item in mainNavItems"
            :key="item.name"
            class="navbar-item"
            href="#"
            @click="selectItem(item.name)"
          >
            <span v-html="item.icon"></span> {{ item.name }}
          </a>
        </div>
      </div>
    </nav>
    <SubNavbar :subItems="subNavItems" />
  </div>
</template>

<script>
import SubNavbar from "./SubNavbar.vue";

export default {
  name: "Navbar",
  components: {
    SubNavbar,
  },
  data() {
    return {
      mainNavItems: [
        { name: "Bar", icon: '<i class="fas fa-cocktail" />' },
        { name: "Construction", icon: '<i class="fas fa-hard-hat" />' },
        { name: "Food", icon: '<i class="fas fa-utensils" />' },
        { name: "Legal", icon: '<i class="fas fa-balance-scale" />' },
        { name: "Restaurant", icon: '<i class="fas fa-utensil-spoon" />' },
        { name: "Wine", icon: '<i class="fas fa-wine-bottle" />' },
      ],
      subNavItems: [],
    };
  },
  methods: {
    selectItem(item) {
      const subNavMapping = {
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
      };
      this.subNavItems = subNavMapping[item] || [];
    },
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
  margin: 0 0.5rem;
}
.navbar-item:hover {
  text-decoration: underline;
}
</style>
