<template>
  <div class="search-bar-container">
    <input 
      :value="city" 
      @input="$emit('update:city', $event.target.value)" 
      placeholder="Enter city" 
      class="search-bar" 
    />

    <!-- State Dropdown -->
    <select 
      :value="state" 
      @change="$emit('update:state', $event.target.value)" 
      class="state-dropdown"
    >
      <option disabled value="">Select a state</option>
      <option v-for="stateAbbr in stateAbbreviations" :key="stateAbbr" :value="stateAbbr">
        {{ stateAbbr }}
      </option>
    </select>

    <!-- Country Dropdown -->
    <select 
      :value="country" 
      @change="$emit('update:country', $event.target.value)" 
      class="country-dropdown"
    >
      <option disabled value="">Select a country</option>
      <option v-for="countryOption in countryList" :key="countryOption" :value="countryOption">
        {{ countryOption }}
      </option>
    </select>

    <button @click="onSearch" class="search-button">Search</button>
  </div>
</template>

<script>
export default {
  props: {
    city: String,
    state: String,
    country: String,
    stateAbbreviations: Array,
    countryList: Array
  },
  emits: ['update:city', 'update:state', 'update:country', 'search'],
  methods: {
    onSearch() {
      this.$emit('search');
    }
  }
}
</script>

<style scoped>
.search-bar-container {
  display: flex;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.search-bar {
  padding: 0.8rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px 0 0 4px;
  outline: none;
  width: 300px;
}

.search-bar:focus {
  border-color: var(--primary-blue);
}

.state-dropdown, .country-dropdown {
  padding: 0.8rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  outline: none;
  margin-left: 1rem;
  width: 150px;
}

.search-button {
  background-color: var(--primary-blue);
  color: white;
  border: none;
  padding: 0.8rem 1rem;
  font-size: 1rem;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background-color: var(--primary-gold);
}
</style>
