<template>
    <div class="places-container">
        <h2>Search Results</h2>
        <ul>
            <li v-for="place in filteredPlaces" :key="place.id">
                {{ place.category }} - {{ place.description }}
            </li>
        </ul>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";

const route = useRoute();
const store = useStore();
const searchText = ref(route.query.searchText || "");

const allPlaces = computed(() => store.state.cityData);
const filteredPlaces = computed(() => {
    const query = searchText.value.trim().toLowerCase();
    if (!query) return [];

    return Object.values(allPlaces.value)
        .flat()
        .filter((place) => {
            return Object.values(place).some((value) =>
                String(value).toLowerCase().includes(query)
            );
        });
});

onMounted(() => {
    searchText.value = route.query.searchText || "";
});
</script>

<style scoped>
.places-container {
    padding: 20px;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin: 10px 0;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
}
</style>
