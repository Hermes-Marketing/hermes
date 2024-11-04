<template>
    <div ref="map" class="map"></div>
</template>

<script>
import * as L from "leaflet";
import "leaflet/dist/leaflet.css";

export default {
    props: {
        coordinates: {
            type: Object,
            required: true,
        },
        cityCompanies: {
            type: Array,
            required: true,
        },
    },
    mounted() {
        const map = L.map(this.$refs.map).setView(this.coordinates, 12);

        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            maxZoom: 19,
        }).addTo(map);

        this.cityCompanies.forEach((company) => {
            L.marker([company.latitude, company.longitude])
                .addTo(map)
                .bindPopup(company.name); // Bind popup with company name
        });
    },
};
</script>

<style scoped>
.map {
    height: 400px;
    width: 100%;
}
</style>
