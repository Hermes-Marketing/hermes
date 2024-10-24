<template>
    <div class="plan-route-container">
        <h1>Plan Your Route</h1>

        <!-- SearchForm Component -->
        <SearchForm
            :city="city"
            :state="state"
            :country="country"
            :stateAbbreviations="stateAbbreviations"
            :countryList="countryList"
            @update:city="city = $event"
            @update:state="state = $event"
            @update:country="country = $event"
            @search="searchCity"
        />

        <!-- Display loading message while the map is being calculated -->
        <p v-if="isLoading" class="loading-message">
            Calculating businesses in {{ city }}, {{ state }}, {{ country }}...
            Please wait.
        </p>

        <!-- Display message if no businesses are found -->
        <p
            v-if="!isLoading && coordinates && !cityCompanies.length"
            class="no-businesses"
        >
            No businesses nearby.
        </p>

        <MapDisplay
            v-if="!isLoading && coordinates && coordinates.length === 2"
            :coordinates="coordinates"
            :cityCompanies="cityCompanies"
        />
    </div>
</template>
<script>
import { ref } from "vue";
import SearchForm from "./SearchForm.vue";
import MapDisplay from "./MapDisplay.vue";
import { getCompaniesByState } from "../services/api";

export default {
    components: { SearchForm, MapDisplay },
    setup() {
        const city = ref("");
        const state = ref("CA");
        const country = ref("United States");
        const coordinates = ref(null); // Coordinates for the city center
        const cityCompanies = ref([]); // List of businesses with lat/lng coordinates
        const isLoading = ref(false); // Loading state

        const stateAbbreviations = ref([
            "AL",
            "AK",
            "AZ",
            "AR",
            "CA",
            "CO",
            "CT",
            "DE",
            "FL",
            "GA",
            "HI",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "OH",
            "OK",
            "OR",
            "PA",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "WA",
            "WV",
            "WI",
            "WY",
        ]);

        const countryList = ref([
            "United States",
            "Canada",
            "United Kingdom",
            "Australia",
            "Germany",
            "France",
            "Italy",
            "Spain",
            "Mexico",
            "Japan",
        ]);

        const searchCity = async () => {
            isLoading.value = true;
            cityCompanies.value = [];
            coordinates.value = null;

            try {
                const response = await getCompaniesByState(state.value);
                if (response && response.data) {
                    const filteredCompanies = response.data.filter(
                        (company) =>
                            company.city.toLowerCase() ===
                            city.value.toLowerCase()
                    );

                    // Geocode the city center
                    const cityCenterUrl = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(
                        city.value + "," + state.value
                    )}&format=json&limit=1`;
                    const cityCenterResponse = await fetch(cityCenterUrl);
                    const cityCenterData = await cityCenterResponse.json();

                    // Ensure city center data exists before accessing lat/lon
                    if (
                        cityCenterData.length > 0 &&
                        cityCenterData[0].lat &&
                        cityCenterData[0].lon
                    ) {
                        coordinates.value = [
                            parseFloat(cityCenterData[0].lat),
                            parseFloat(cityCenterData[0].lon),
                        ];
                        console.log("City Center:", coordinates.value);
                    } else {
                        console.error("City center geocode data not found");
                    }

                    // Geocode each business
                    for (let company of filteredCompanies) {
                        const address = `${company.street_address}, ${company.city}, ${company.state}, ${company.zip_code}`;
                        const geocodeUrl = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(
                            address
                        )}&format=json&limit=1`;
                        const geocodeResponse = await fetch(geocodeUrl);
                        const geocodeData = await geocodeResponse.json();

                        // Ensure geocode data exists before accessing lat/lon
                        if (
                            geocodeData.length > 0 &&
                            geocodeData[0].lat &&
                            geocodeData[0].lon
                        ) {
                            company.latitude = parseFloat(geocodeData[0].lat);
                            company.longitude = parseFloat(geocodeData[0].lon);
                            console.log("Company:", company);
                            cityCompanies.value.push(company);
                        } else {
                            console.error(
                                `Geocode data not found for address: ${address}`
                            );
                        }
                    }
                }
            } catch (error) {
                console.error("Error during search:", error);
            } finally {
                isLoading.value = false;
            }
        };

        return {
            city,
            state,
            country,
            coordinates,
            cityCompanies,
            isLoading,
            stateAbbreviations,
            countryList,
            searchCity,
        };
    },
};
</script>

<style scoped>
.plan-route-container {
    text-align: center;
    padding: 2rem;
}

.loading-message {
    font-size: 1.2rem;
    color: blue;
}

.no-businesses {
    color: red;
    font-size: 1.2rem;
}
</style>
