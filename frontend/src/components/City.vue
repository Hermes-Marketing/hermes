<template>
    <div>
        <h1>{{ cityName }}</h1>
        <ul>
            <li v-for="company in cityData" :key="company.business_name">
                {{ company.business_name }} - {{ company.business_location }}
            </li>
        </ul>
    </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { computed } from "vue";

const route = useRoute();
const store = useStore();
const cityName = route.params.name;
const cityData = computed(() => store.getters.getCityData(cityName));
</script>
