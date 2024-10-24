<template>
    <div class="near-me-container">
        <h2>Businesses Near Me</h2>

        <p v-if="isLoading" class="loading-message">
            Fetching your location and nearby businesses...
        </p>

        <p v-if="!isLoading && !coordinates" class="error-message">
            Unable to get your location.
        </p>

        <MapDisplay
            v-if="!isLoading && coordinates && coordinates.length === 2"
            :coordinates="coordinates"
            :cityCompanies="cityCompanies"
        />

        <p
            v-if="!isLoading && coordinates && !cityCompanies.length"
            class="no-businesses"
        >
            No businesses found within 100km.
        </p>
    </div>
</template>

<script>
import { ref, onMounted } from "vue";
import MapDisplay from "./MapDisplay.vue";
import { getCompanies } from "../services/api"; // Example function for fetching all businesses

export default {
    components: { MapDisplay },
    setup() {
        const coordinates = ref(null); // Store user's current coordinates
        const cityCompanies = ref([]); // Store nearby businesses
        const isLoading = ref(true); // Loading state

        // Calculate the distance between two coordinates (Haversine formula)
        const calculateDistance = (lat1, lon1, lat2, lon2) => {
            const R = 6371; // Radius of the earth in km
            const dLat = ((lat2 - lat1) * Math.PI) / 180;
            const dLon = ((lon2 - lon1) * Math.PI) / 180;
            const a =
                Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                Math.cos((lat1 * Math.PI) / 180) *
                    Math.cos((lat2 * Math.PI) / 180) *
                    Math.sin(dLon / 2) *
                    Math.sin(dLon / 2);
            const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
            const distance = R * c; // Distance in km
            return distance;
        };

        const fetchNearbyBusinesses = async () => {
            isLoading.value = true;
            try {
                const response = await getCompanies(); // Fetch all businesses from the backend
                console.log("Fetched Businesses:", response.data); // Log the businesses array

                // Access the array of businesses from the response
                const allBusinesses = response.data; // Since data is already an array, you can assign it directly

                const filteredBusinesses = [];

                // Filter businesses within 100km radius
                allBusinesses.forEach((business) => {
                    const distance = calculateDistance(
                        coordinates.value[0],
                        coordinates.value[1],
                        business.latitude,
                        business.longitude
                    );
                    if (distance <= 100) {
                        filteredBusinesses.push(business);
                    }
                });

                cityCompanies.value = filteredBusinesses;
            } catch (error) {
                console.error("Error fetching businesses:", error);
            } finally {
                isLoading.value = false;
            }
        };

        // Get user's current location
        const getCurrentLocation = () => {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        coordinates.value = [
                            position.coords.latitude,
                            position.coords.longitude,
                        ];
                        fetchNearbyBusinesses(); // Fetch businesses after location is set
                    },
                    (error) => {
                        console.error("Error getting location:", error);
                        isLoading.value = false;
                    }
                );
            } else {
                console.error("Geolocation is not supported by this browser.");
                isLoading.value = false;
            }
        };

        onMounted(() => {
            getCurrentLocation();
        });

        return {
            coordinates,
            cityCompanies,
            isLoading,
        };
    },
};
</script>

<style scoped>
.near-me-container {
    text-align: center;
    padding: 2rem;
}

.loading-message {
    font-size: 1.2rem;
    color: blue;
}

.error-message {
    font-size: 1.2rem;
    color: red;
}

.no-businesses {
    color: red;
    font-size: 1.2rem;
}
</style>
