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
    align-items: center; /* Align items vertically */
    margin-bottom: 1.5rem;
    gap: 1rem; /* Add space between components */
}

.search-bar {
    padding: 0.8rem; /* Padding for input */
    font-size: 1rem; /* Font size */
    border: 1px solid #ccc; /* Border for input */
    border-radius: 8px; /* Rounded corners */
    outline: none; /* Remove default outline */
    width: 300px; /* Fixed width */
    transition: border-color 0.3s ease, box-shadow 0.3s ease; /* Smooth transition */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Shadow for depth */
}

.search-bar:focus {
    border-color: var(--primary-blue); /* Focus border color */
    box-shadow: 0 0 5px rgba(0, 102, 204, 0.5); /* Glow effect on focus */
}

.search-bar:hover {
    border-color: var(--primary-blue); /* Hover border color */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* Darker shadow on hover */
}

/* Style for the dropdown component */
.state-dropdown,
.country-dropdown {
    width: 150px; /* Fixed width for dropdowns */
    border: 1px solid #ccc; /* Border for dropdowns */
    border-radius: 8px; /* Rounded corners */
    background-color: white; /* Background color */
    padding: 0.4rem; /* Padding for dropdowns */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Shadow for depth */
    transition: border-color 0.3s ease, box-shadow 0.3s ease; /* Smooth transition */
}

/* Dropdown styles on focus */
.state-dropdown:focus,
.country-dropdown:focus {
    border-color: var(--primary-blue); /* Focus border color */
    box-shadow: 0 0 5px rgba(0, 102, 204, 0.5); /* Glow effect on focus */
}

/* Hover effect for dropdowns */
.state-dropdown:hover,
.country-dropdown:hover {
    border-color: var(--primary-blue); /* Hover border color */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* Darker shadow on hover */
}

/* Styling for dropdown options */
.p-dropdown-item {
    padding: 0.8rem; /* Padding for options */
    border-bottom: 1px solid #eee; /* Divider between options */
    transition: background-color 0.2s ease; /* Smooth transition for hover effect */
}

.p-dropdown-item:hover {
    background-color: var(--primary-blue); /* Background color on hover */
    color: white; /* Change text color on hover */
}

/* Styling for the selected item */
.p-dropdown-label {
    padding: 0.8rem; /* Padding for selected label */
    border-radius: 8px; /* Rounded corners */
    background-color: #f9f9f9; /* Background for selected item */
    color: #333; /* Text color */
}

/* Customize the dropdown arrow */
.p-dropdown .p-dropdown-trigger {
    background-color: transparent; /* Make background transparent */
    border: none; /* Remove border */
    cursor: pointer; /* Pointer cursor */
}
.search-button {
    background-color: var(--primary-blue);
    color: black; /* Change text color to white */

    border: 1px solid #ccc; /* Border for input */
    padding: 0.8rem 1.2rem; /* Increased padding */
    font-size: 1rem;
    border-radius: 8px; /* More rounded corners */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease; /* Added transform effect */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15); /* Added shadow */
}

.search-button:hover {
    background-color: var(--primary-gold);
    transform: translateY(-2px); /* Lift effect on hover */
}

.search-button:active {
    transform: translateY(1px); /* Push effect on click */
}
</style>
