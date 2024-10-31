<template>
    <div class="home-container">
        <div class="search-box">
            <InputText
                class="search-bar"
                placeholder="What are you looking for?"
                @keyup.enter="searchPlaces"
                v-model="searchText"
            />
        </div>
        <div class="cities">
            <h2>Cities</h2>
            <div class="city-grid">
                <div
                    v-for="city in uniqueCities"
                    :key="city"
                    class="city-item"
                    @click="goToCity(city)"
                >
                    <div class="city-image"></div>
                    <div class="city-name">{{ city }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import InputText from "primevue/inputtext";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { getCompanies } from "../services/api";

const uniqueCities = ref([]);
const cityData = ref({});
const searchText = ref("");
const router = useRouter();
const store = useStore();

onMounted(async () => {
    console.log("onMounted hook called");
    const response = await getCompanies();
    console.log("API response:", response);
    const cities = response.data.map((company) => company.city);
    console.log("Extracted cities:", cities);
    uniqueCities.value = [...new Set(cities)].sort();
    console.log("Unique cities:", uniqueCities.value);
    cityData.value = response.data.reduce((acc, company) => {
        if (!acc[company.city]) {
            acc[company.city] = [];
        }
        acc[company.city].push(company);
        return acc;
    }, {});
    console.log("City data:", cityData.value);
    store.dispatch("updateCityData", cityData.value);
    console.log("City data dispatched to store");
});

const goToCity = (city) => {
    console.log("Navigating to city:", city);
    router.push(`/city/${city}`);
};

const searchPlaces = () => {
    const query = searchText.value.trim().toLowerCase();
    if (query) {
        router.push(`/places?searchText=${encodeURIComponent(query)}`);
    }
};
</script>

<style scoped>
.search-bar {
    @apply w-96 p-2 border border-gray-300 rounded-full focus:border-black focus:outline-none;
    margin-bottom: 20vh;
}

.home-container {
    display: flex;
    flex-direction: column;
    margin-top: 20vh;
    height: 100%;
    background-color: #f1c400; /* PANTONE 7406 C */
}

.search-box {
    flex: 0 0 30%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    background-color: #ffffff;
}

.cities {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 1.5em;
    font-family: Geller Text Regular;
    color: #002b49; /* PANTONE 7463 C */
}

.city-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr); /* 6 cities per row */
    gap: 20px;
    justify-items: center;
}

.city-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
    background-color: #ffffff;
    padding: 20px;
    border: 1px solid #002b49; /* PANTONE 7463 C */
    border-radius: 10px;
}

.city-image {
    width: 100px;
    height: 100px;
    background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwi7yz1k2ejMWDE_J6CVgbRtmaom-A8TEH-w&s");
    background-size: cover;
    background-position: center;
    border-radius: 50%;
    margin-bottom: 10px;
}

.city-name {
    color: #6f2c3f; /* PANTONE 505 C */
    transition: color 0.3s;
    font-family: Geller Text Bold;
    font-size: 1.2em;
}

.city-name:hover {
    color: #002b49; /* PANTONE 7463 C */
}
</style>
