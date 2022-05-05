'use strict';

// We use a function declaration for initMap because we actually *do* need
// to rely on value-hoisting in this circumstance.
function initMap() {
  const sfBayCoords = {
    lat: 37.601773,
    lng: -122.20287,
  };

  const basicMap = new google.maps.Map(document.querySelector('#map'), {
    center: sfBayCoords,
    zoom: 12,
  });

  const sfMarker = new google.maps.Marker({
    position: sfBayCoords,
    title: 'SF Bay',
    map: basicMap,
  });

  sfMarker.addListener('click', () => {
    alert('Hi!');
  });

  const sfInfo = new google.maps.InfoWindow({
    content: '<h1>San Mateo Bridge</h1>',
  });

  sfInfo.open(basicMap, sfMarker);

  const locations = [
    {
      name: 'Hackbright Academy',
      coords: {
        lat: 37.7887459,
        lng: -122.4115852,
      },
    },
    {
      name: 'Powell Street Station',
      coords: {
        lat: 37.7844605,
        lng: -122.4079702,
      },
    },
    {
      name: 'Montgomery Station',
      coords: {
        lat: 37.7894094,
        lng: -122.4013037,
      },
    },
  ];

  const markers = [];
  for (const location of locations) {
    markers.push(
      new google.maps.Marker({
        position: location.coords,
        title: location.name,
        map: basicMap,
        icon: {
          // custom icon
          url: '/static/img/marker.svg',
          scaledSize: {
            width: 30,
            height: 30,
          },
        },
      }),
    );
  }

  for (const marker of markers) {
    const markerInfo = `
      <h1>${marker.title}</h1>
      <p>
        Located at: <code>${marker.position.lat()}</code>,
        <code>${marker.position.lng()}</code>
      </p>
    `;

    const infoWindow = new google.maps.InfoWindow({
      content: markerInfo,
      maxWidth: 200,
    });

    marker.addListener('click', () => {
      infoWindow.open(basicMap, marker);
    });
  }
}

// navigator.geolocation.getCurrentPosition(
//   position => console.log(position.coords),
//   err => console.log(err)
// );
