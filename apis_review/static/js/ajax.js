'use strict';

const handleForm = (evt) => {
    evt.preventDefault();

    const query = document.querySelector('#query').value;
    const queryString = new URLSearchParams({ query }).toString();

    fetch(`/places.json?${queryString}`)
    .then((response) => response.json())
    .then((resultsJSON) => {
        // console.log(resultsJSON);

        const resultsDiv = document.querySelector('#search-results');
        resultsDiv.innerHTML = '';

        for (const res of resultsJSON.results) {
            let src = 'https://upload.wikimedia.org/wikipedia/commons/a/aa/Google_Maps_icon_%282020%29.svg';
            let alt = 'default image';
            if ('photos' in res) {
                src = resultsJSON.photos_url + res.photos[0].photo_reference;
                alt = `${res.name} image`;
            }

            const newHTML =
            `<div class="card mx-auto mb-2" style="width: 18rem;">
                <img class="card-img-top" src="${src}" alt="${alt}">

                <div class="card-body">
                    <h5 class="card-title">${res.name}</h5>
                    <p class="card-text">${res.formatted_address}</p>
                    <p class="card-text">
                        Lat.: ${res.geometry.location.lat}<br>
                        Long.: ${res.geometry.location.lng}
                    </p>
                </div>
            </div>`;

            resultsDiv.insertAdjacentHTML('beforeend', newHTML);
        }
    });
};

document.querySelector('#ajax-form').addEventListener('submit', handleForm);
