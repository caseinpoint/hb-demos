'use strict';

// We chose to attach all our event listeners in this function since this is
// where the `map` object is in-scope.
//
// There are other ways to do this. Another way to make sure `map` is in-scope
// is to define functions outside of `initMap` that take in a Google Map
// object as an argument.
function initMap() {
  const map = new google.maps.Map(document.querySelector('#map'), {
    center: {
      lat: 37.601773,
      lng: -122.20287,
    },
    zoom: 11,
  });

  // Apply custom styles to a map. In this example, we make the
  // water "wine dark sea".
  document.querySelector('#custom-style').addEventListener('click', () => {
    const customStyledMap = new google.maps.StyledMapType([
      {
        featureType: 'water',
        elementType: 'geometry.fill',
        stylers: [{ color: '#722F37' }],
      },
    ]);

    map.mapTypes.set('styled_map', customStyledMap);
    map.setMapTypeId('styled_map');
  });

  // Ask user to enter a location. Geocode the location to get its coordinates
  // and drop a marker onto the map.
  document.querySelector('#geocode-address').addEventListener('click', () => {
    const userAddress = prompt('Enter a location');

    const geocoder = new google.maps.Geocoder();
    geocoder.geocode({ address: userAddress }, (results, status) => {
      if (status === 'OK') {
        // Get the coordinates of the user's location
        const userLocation = results[0].geometry.location;
        console.log(results);

        // Create a marker
        const userMarker = new google.maps.Marker({
          position: userLocation,
          map: map,
        });

        // Zoom in on the geolocated location
        map.setCenter(userLocation);
        map.setZoom(14);

        // Add an InfoWindow to the marker
        const userInfo = new google.maps.InfoWindow({
          content: `<div>
            <h2>${userAddress}</h2>
            <h3>coords: ${userLocation}</h3>
          </div>`
        });
        userInfo.open(map, userMarker);
      } else {
        alert(`Geocode was unsuccessful for the following reason: ${status}`);
      }
    });
  });

  // Center the map on the user's current geolocation.
  document.querySelector('#current-location').addEventListener('click', () => {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const userLocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };

        map.setCenter(userLocation);
        map.setZoom(14);
      },
      (error) => { alert(`ERROR(${error.code}): ${error.message}`); }
    );
  });

  // Draw a line on the map from Hackbright to Powell Street Station to
  // Montgomery Station
  document.querySelector('#draw-polyline').addEventListener('click', () => {
    const polyline = new google.maps.Polyline({
      path: [
        {
          lat: 37.7887459, // Hackbright
          lng: -122.4115852,
        },
        {
          lat: 37.7844605, // Powell Street Station
          lng: -122.4079702,
        },
        {
          lat: 37.7894094, // Montgomery Station
          lng: -122.4013037,
        },
      ],
      geodesic: true,
      strokeColor: '#ff0000',
      strokeOpacity: 1.0,
      strokeWeight: 5,
    });

    polyline.setMap(map);
    map.setCenter({lat: 37.7844605, lng: -122.4079702});
    map.setZoom(16);
  });

  // Display walking directions from Hackbright to Powell Street Station
  // on the map
  document.querySelector('#display-directions').addEventListener('click', () => {
    const directionsService = new google.maps.DirectionsService();

    // The DirectionsRenderer object is in charge of drawing directions
    // on maps
    const directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);

    const hbToPowellRoute = {
      origin: {
        lat: 37.7887459,
        lng: -122.4115852,
      },
      destination: {
        lat: 37.7844605,
        lng: -122.4079702,
      },
      travelMode: 'WALKING',
    };

    directionsService.route(hbToPowellRoute, (response, status) => {
      if (status === 'OK') {
        directionsRenderer.setDirections(response);
      } else {
        alert(`Directions request unsuccessful due to: ${status}`);
      }
    });
  });
}
