<script setup lang="ts">
import '@maptiler/sdk/dist/maptiler-sdk.css';
import { Map, MapStyle, config, Marker, Popup } from '@maptiler/sdk';
import { shallowRef, watch, onUnmounted, markRaw } from 'vue';
import {
  MAP_ACCESS_TOKEN,
  DEFAULT_INTIAL_ZOOM,
  PRIMARY_MARKER_COLOR,
  SECONDARY_MARKER_COLOR,
} from '@/shared/constants';
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
  const filteredPositions = Object.values(updatedProps.positions).filter(
    (position) => position.id !== updatedProps?.selectedPosition?.id,
  );
  config.apiKey = MAP_ACCESS_TOKEN;
  map.value = markRaw(
    new Map({
      container: mapContainer.value,
      style: MapStyle.STREETS,
      center: initialPosition,
      zoom: DEFAULT_INTIAL_ZOOM,
    }),
  );
  const selectedPositionPopup = new Popup({ offset: 25 }).setText(
    `Property ID: ${updatedProps.selectedPosition.id}`,
  );
  new Marker({ color: PRIMARY_MARKER_COLOR })
    .setLngLat(initialPosition)
    .setPopup(selectedPositionPopup)
    .addTo(map.value);
  filteredPositions.forEach((position) => {
    const locationPopup = new Popup({ offset: 25 }).setText(`Property ID: ${position.id}`);
    new Marker({ color: SECONDARY_MARKER_COLOR, scale: 0.7, opacity: '0.8' })
      .setLngLat([position.longitude, position.latitude])
      .setPopup(locationPopup)
      .addTo(map.value);
  });
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
