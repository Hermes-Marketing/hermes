<template>
  <div class="map-wrapper">
    <l-map
      ref="mapRef"
      :zoom="zoomLevel"
      :center="cityCoordinates"
      class="map-container"
      @update:zoom="updateZoom"
    >
      <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

      <!-- Render a pin for each business at their location -->
      <l-marker 
        v-for="company in cityCompanies"
        :key="company.business_name"
        :lat-lng="[company.latitude, company.longitude]"
      >
        <l-popup>{{ company.business_name }}</l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup } from "vue3-leaflet";
import "leaflet/dist/leaflet.css";
import { latLngBounds } from "leaflet";

export default {
  props: {
    cityCoordinates: Array,  // Coordinates for the city center [latitude, longitude]
    cityCompanies: Array     // List of companies with lat/lng coordinates
  },
  data() {
    return {
      zoomLevel: 13  // Default zoom level
    };
  },
  watch: {
    cityCompanies: {
      immediate: true,
      handler(companies) {
        if (companies.length > 0) {
          this.adjustZoomToFitMarkers(companies);
        }
      }
    }
  },
  methods: {
    adjustZoomToFitMarkers(companies) {
      const bounds = latLngBounds(this.cityCoordinates);  // Start with city center as initial bounds

      // Expand bounds to include all business coordinates
      companies.forEach(company => {
        bounds.extend([company.latitude, company.longitude]);
      });

      // Adjust the zoom level to fit all markers with extra padding
      if (this.$refs.mapRef) {
        this.$refs.mapRef.fitBounds(bounds, { padding: [100, 100], maxZoom: 8 });
      }
    },
    updateZoom(newZoom) {
      this.zoomLevel = newZoom;
    }
  },
  components: { LMap, LTileLayer, LMarker, LPopup }
};
</script>

<style scoped>
.map-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 600px; /* Adjust the height based on your layout */
}

.map-container {
  height: 100%;
  width: 600px;  /* Adjust the width to make it square */
  margin: 0 auto;
  border: 2px solid var(--primary-blue);
  border-radius: 8px;
}
</style>
