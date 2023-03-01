function initMap(mapboxKey) {
    console.log(mapboxKey);
}

fetch('/api/mapboxkey')
.then((res) => res.text())
.then((key) => { initMap(key); });