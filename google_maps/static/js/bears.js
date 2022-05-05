'use strict';

function initMap() {
  const map = new google.maps.Map(document.querySelector('#map'), {
    center: {
      lat: 72,
      lng: -140,
    },
    scrollwheel: false,
    zoom: 5,
    zoomControl: true,
    panControl: false,
    streetViewControl: false,
    styles: MAPSTYLES, // mapStyles is defined in mapstyles.js
    mapTypeId: google.maps.MapTypeId.TERRAIN,
  });

  // When a user clicks on a bear, an info window about that bear will appear.
  //
  // When they click on another bear, we want the previous info window to
  // disappear, so that only one window is open at a time.
  //
  // To do this, we'll define a single InfoWindow instance. All markers will
  // share this instance.
  const bearInfo = new google.maps.InfoWindow();

  // Retrieving the information with AJAX.
  //
  // If you want to see what `/api/bears` returns, you should check `server.py`
  fetch('/api/bears')
    .then((response) => response.json())
    .then((bears) => {
      for (const bear of bears) {
        // Define the content of the infoWindow
        const bearInfoContent = `
        <div class="window-content">
          <div class="bear-thumbnail">
            <img
              src="/static/img/polarbear.jpg"
              alt="polarbear"
            />
          </div>

          <ul class="bear-info">
            <li><b>Bear gender: </b>${bear.gender}</li>
            <li><b>Bear birth year: </b>${bear.birthYear}</li>
            <li><b>Year captured: </b>${bear.capYear}</li>
            <li><b>Collared: </b>${bear.collared}</li>
            <li><b>Location: </b>${bear.capLat}, ${bear.capLong}</li>
          </ul>
        </div>
      `;

        const bearMarker = new google.maps.Marker({
          position: {
            lat: bear.capLat,
            lng: bear.capLong,
          },
          title: `Bear ID: ${bear.bearId}`,
          icon: {
            url: '/static/img/polarBear.svg',
            scaledSize: new google.maps.Size(50, 50),
          },
          map, // same as saying map: map
        });

        bearMarker.addListener('click', () => {
          bearInfo.close();
          bearInfo.setContent(bearInfoContent);
          bearInfo.open(map, bearMarker);
        });
      }
    })
    .catch(() => {
      alert(`
      We were unable to retrieve data about bears :(

      Did you remember to create the bears database and seed it?
      (See model.py and seed.py for more info).
    `);
    });

  // Google Maps also provides a built-in control panel that allows users to
  // toggle different map styles.
  //
  // Here's how you do it:
  //
  // Create a new StyledMapType object, passing it the array of styles,
  // as well as the name of the map style.
  //
  // The name will be displayed in a button on the map-type control panel.
  //
  // const styledMap = new google.maps.StyledMapType(
  //  MAPSTYLES,
  //  { name: "Arctic Map" }
  // );
  //
  // You would then set 'styles' in Map() constructor's options to 'styledMap'.
  // For example:
  //
  // const map = new google.maps.Map(document.getElementById('bear-map', {
  //   center: mapCenter,
  //   // ... etc.
  //   styles: styledMap
  // });
  //
  // Finally, you must associate the styled map with the MapTypeId and
  // set it to display.
  //
  // map.mapTypes.set('map_style', styledMap);
  // map.setMapTypeId('map_style');
}
