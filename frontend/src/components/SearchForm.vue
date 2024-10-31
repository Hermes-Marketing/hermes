<template>
    <div class="search-bar-container">
        <!-- City Input -->
        <InputText
            v-model="city"
            placeholder="Enter city"
            class="search-bar"
            @input="updateCity"
        />

        <!-- State Dropdown -->

        <Dropdown
            v-model="selectedState"
            :options="stateOptions"
            optionLabel="label"
            placeholder="Select a state"
            class="state-dropdown"
            @change="updateState"
        />

        <!-- Country Dropdown -->
        <Dropdown
            v-model="selectedCountry"
            :options="countryOptions"
            optionLabel="label"
            placeholder="Select a country"
            class="country-dropdown"
            @change="updateCountry"
        />

        <!-- Search Button -->
        <Button label="Search" class="search-button" @click="onSearch"
            >Search</Button
        >
    </div>
</template>
<script setup>
import { defineProps, defineEmits, ref, watch } from "vue";
import InputText from "primevue/inputtext";
import Dropdown from "primevue/dropdown";
import Button from "primevue/button";

// Define props
const props = defineProps({
    city: String,
    state: String,
    country: String,
    stateAbbreviations: Array,
    countryList: Array,
});

// Define emits
const emit = defineEmits([
    "update:city",
    "update:state",
    "update:country",
    "search",
]);

// Reactive state for city, state, and country
const city = ref(props.city);
const selectedState = ref({ label: props.state, value: props.state });
const selectedCountry = ref({ label: props.country, value: props.country });

// Prepare options for dropdowns
const stateOptions = props.stateAbbreviations.map((abbr) => ({
    label: abbr,
    value: abbr,
}));
const countryOptions = props.countryList.map((option) => ({
    label: option,
    value: option,
}));

// Watchers to emit changes for city
watch(city, (newValue) => {
    emit("update:city", newValue);
});

// Watchers to emit changes for state and country as strings
watch(selectedState, (newValue) => {
    emit("update:state", newValue.value); // Emit only the value (String)
});

watch(selectedCountry, (newValue) => {
    emit("update:country", newValue.value); // Emit only the value (String)
});

// Method to emit search event
const onSearch = () => {
    emit("search");
};

// Update methods for inputs
const updateCity = (event) => {
    city.value = event.target.value;
};

const updateState = (event) => {
    selectedState.value = event.value; // Update with the value selected
};

const updateCountry = (event) => {
    selectedCountry.value = event.value; // Update with the value selected
};
</script>
<style scoped>
.search-bar-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 1.5rem;
    gap: 1rem;
    font-family: Geller Text Regular;
    background-color: #f1c400; /* PANTONE 7406 C */
}

.search-bar {
    padding: 0.8rem;
    font-size: 1rem;
    border: 1px solid #002b49; /* PANTONE 7463 C */
    border-radius: 8px;
    outline: none;
    width: 300px;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    font-family: Geller Text Regular;
    background-color: #ffffff;
}

.search-bar:focus {
    border-color: #00a3e0; /* PANTONE 299 C */
    box-shadow: 0 0 5px rgba(0, 163, 224, 0.5);
}

.search-bar:hover {
    border-color: #00a3e0; /* PANTONE 299 C */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

/* Style for the dropdown component */
.state-dropdown,
.country-dropdown {
    width: 150px;
    border: 1px solid #002b49; /* PANTONE 7463 C */
    border-radius: 8px;
    background-color: #ffffff;
    padding: 0.4rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
    font-family: Geller Text Regular;
}

/* Dropdown styles on focus */
.state-dropdown:focus,
.country-dropdown:focus {
    border-color: #00a3e0; /* PANTONE 299 C */
    box-shadow: 0 0 5px rgba(0, 163, 224, 0.5);
}

/* Hover effect for dropdowns */
.state-dropdown:hover,
.country-dropdown:hover {
    border-color: #00a3e0; /* PANTONE 299 C */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

/* Styling for dropdown options */
.p-dropdown-item {
    padding: 0.8rem;
    border-bottom: 1px solid #eee;
    transition: background-color 0.2s ease;
    font-family: Geller Text Regular;
}

.p-dropdown-item:hover {
    background-color: #00a3e0; /* PANTONE 299 C */
    color: #ffffff;
}

/* Styling for the selected item */
.p-dropdown-label {
    padding: 0.8rem;
    border-radius: 8px;
    background-color: #f1c400; /* PANTONE 7406 C */
    color: #002b49; /* PANTONE 7463 C */
    font-family: Geller Text Bold;
}

/* Customize the dropdown arrow */
.p-dropdown .p-dropdown-trigger {
    background-color: transparent;
    border: none;
    cursor: pointer;
}

.search-button {
    background-color: #00a3e0; /* PANTONE 299 C */
    color: #ffffff;
    border: 1px solid #002b49; /* PANTONE 7463 C */
    padding: 0.8rem 1.2rem;
    font-size: 1rem;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
    font-family: Geller Text Bold;
}

.search-button:hover {
    background-color: #ffd141; /* PANTONE 122 C */
    transform: translateY(-2px);
}

.search-button:active {
    transform: translateY(1px);
}
</style>
