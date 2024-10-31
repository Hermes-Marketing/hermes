<template>
    <div class="places-container">
        <h2>Search Results</h2>
        <div class="cards-container">
            <div v-for="place in filteredPlaces" :key="place.id" class="card">
                <img
                    :src="
                        place.image ||
                        'https://sigmachi.org/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-12.33.50-PM-239x300.png'
                    "
                />
                <div class="card-content">
                    <h3>{{ place.category }}</h3>
                    <p>{{ truncateText(place.description, 120) }}</p>
                </div>
            </div>
        </div>
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

function truncateText(text, length) {
    if (text?.length > length) {
        return text.substring(0, length) + "...";
    }
    return text || "Update text...";
}

onMounted(() => {
    searchText.value = route.query.searchText || "";
});
</script>

<style scoped>
.places-container {
    padding: 20px;
    font-family: Geller Text Regular;
    background-color: #f1c400; /* PANTONE 7406 C */
}

.cards-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    margin: 20px;
    width: 300px;
    height: 300px;
    border: 1px solid #002b49; /* PANTONE 7463 C */
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.card img {
    width: 100px;
    height: 125px;
    object-fit: cover;

    margin-top: 20px;
}

.card-content {
    padding: 20px;
    text-align: center;
}

.card-content h3 {
    font-family: Geller Text Bold;
    color: #002b49; /* PANTONE 7463 C */
    margin-bottom: 10px;
}

.card-content p {
    font-family: Geller Text Regular;
    color: #6f2c3f; /* PANTONE 505 C */
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>
