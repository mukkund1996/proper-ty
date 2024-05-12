<script setup lang="ts">
import '@maptiler/sdk/dist/maptiler-sdk.css';
import { Map, MapStyle, config, Marker } from '@maptiler/sdk';
import { shallowRef, watch, onUnmounted, markRaw } from 'vue';
import { MAP_ACCESS_TOKEN, DEFAULT_INTIAL_ZOOM, MARKER_COLOR } from '@/shared/constants';
import type { Location } from '@/models/property';

const props = defineProps<{
  positions: Record<number, Location>;
  selectedPosition?: Location;
}>();

const mapContainer = shallowRef();
const map = shallowRef();

watch(props, (updatedProps) => {
  if (!updatedProps.selectedPosition) {
    return;
  }
  const initialPosition: [number, number] = [
    updatedProps.selectedPosition.longitude,
    updatedProps.selectedPosition.latitude,
  ];
  config.apiKey = MAP_ACCESS_TOKEN;
  map.value = markRaw(
    new Map({
      container: mapContainer.value,
      style: MapStyle.STREETS,
      center: initialPosition,
      zoom: DEFAULT_INTIAL_ZOOM,
    }),
  );
  new Marker({ color: MARKER_COLOR }).setLngLat(initialPosition).addTo(map.value);
});
onUnmounted(() => {
  map.value?.remove();
});
</script>

<template>
  <div class="map-wrap">
    <div class="map" ref="mapContainer"></div>
  </div>
</template>

<style scoped>
.map-wrap {
  position: relative;
  width: 45%;
  height: calc(100vh - 500px);
  margin-right: 1.2rem;
}

.map {
  position: absolute;
  width: 100%;
  height: 100%;
}
</style>
