<template>
  <div>
    <h1>Explore Categories</h1>
    <!-- Updated Category Grid -->
    <div class="category-grid">
      <button v-for="category in categories" :key="category" @click="filterByCategory(category)" class="category-card">
        {{ category }}
      </button>
      <button @click="resetFilter" class="category-card">All Categories</button> <!-- Add a reset button to show all -->
    </div>

    <h2>Companies</h2>
    <!-- Updated Company Card Grid -->
    <div class="company-grid">
      <CompanyCard v-for="company in filteredCompanies" :key="company.email_address" :company="company" class="company-card" />
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import CompanyCard from './CompanyCard.vue';
import { getCompanies } from '@/services/api';

export default {
  components: { CompanyCard },
  setup() {
    const companies = ref([]);
    const filteredCompanies = ref([]);
    const categories = ref([]);
    const activeCategory = ref(null); // Track the active category

    onMounted(async () => {
      const response = await getCompanies();
      if (response && response.data) {
        companies.value = response.data;
        filteredCompanies.value = companies.value;
        categories.value = [...new Set(companies.value.map(company => company.category))]; // Unique categories
      }
    });

    const filterByCategory = (category) => {
      activeCategory.value = category; // Set the active category
      filteredCompanies.value = companies.value.filter(company => company.category === category); // Filter based on category
    };

    const resetFilter = () => {
      activeCategory.value = null; // Reset the active category
      filteredCompanies.value = companies.value; // Show all companies
    };

    return {
      companies,
      filteredCompanies,
      categories,
      activeCategory,
      filterByCategory,
      resetFilter
    };
  }
};
</script>

<style scoped>
/* Category Grid Styling */
.category-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin-top: 1.5rem;
  width: 100%; /* Ensure it takes full width */
}

/* Category Cards */
.category-card {
  background-color: var(--primary-blue);
  color: white;
  border: none;
  padding: 0.8rem;
  font-size: 1rem;
  font-family: var(--font-family);
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.category-card:hover {
  background-color: var(--primary-gold);
  transform: translateY(-2px);
}

/* Company Grid Styling */
.company-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
  width: 100%; /* Ensure it takes full width */
}

/* Company Cards */
.company-card {
  background-color: #fff;
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}

.company-card:hover {
  transform: translateY(-2px);
}

h1 {
  color: var(--primary-blue);
  font-size: 2rem;
  text-align: center;
  margin-bottom: 1.5rem;
}

h2 {
  color: var(--primary-blue);
  font-size: 1.5rem;
  margin-top: 2rem;
  text-align: center;
}
</style>
