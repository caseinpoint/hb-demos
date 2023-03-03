"use strict";

const sfBayCoords = {
  lat: 37.691537,
  lng: -122.310435,
};

const locations = [
  {
    name: "Hackbright Academy",
    coords: {
      lat: 37.7887459,
      lng: -122.4115852,
    },
  },
  {
    name: "Powell Street Station",
    coords: {
      lat: 37.7844605,
      lng: -122.4079702,
    },
  },
  {
    name: "Montgomery Station",
    coords: {
      lat: 37.7894094,
      lng: -122.4013037,
    },
  },
];


function initMap(mapboxKey) {
  mapboxgl.accessToken = mapboxKey;
  
  const sfLngLat = [sfBayCoords.lng, sfBayCoords.lat];

  const map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/examples/cjgiiz9ck002j2ss5zur1vjji",
    center: sfLngLat,
    zoom: 10.5,
  });

  const nav = new mapboxgl.NavigationControl();
  map.addControl(nav, 'bottom-right');

  const sfMarker = new mapboxgl.Marker()
    .setLngLat(sfLngLat)
    .setPopup(new mapboxgl.Popup().setHTML('<h1>San Francisco Bay</h1>'))
    .addTo(map)
    .togglePopup();

  for (const location of locations) {
    const lngLat = [location.coords.lng, location.coords.lat];
    const html = `
      <h1>${location.name}</h1>
      <p>
        Located at: <code>${lngLat[1]}</code>,
        <code>${lngLat[0]}</code>
      </p>
    `;

    const marker = new mapboxgl.Marker()
      .setLngLat(lngLat)
      .setPopup(new mapboxgl.Popup().setHTML(html))
      .addTo(map);
  }
}


// Fetch the api key from the server
fetch("/api/mapboxkey")
  .then((res) => {
    return res.text();
  })
  .then((key) => {
    initMap(key);
  });
