'use strict';

const handleInput = (evt) => {
    const query = evt.target.value;
    if (query.length > 0) {
        const queryString = new URLSearchParams({ query }).toString();

        fetch(`/autocomplete.json?${queryString}`)
        .then((response) => response.json())
        .then((resultsArray) => {
            console.log(resultsArray);

            const dataList = document.querySelector('#autocomplete');
            dataList.innerHTML = '';

            for (const description of resultsArray) {
                const opt = document.createElement('option');
                opt.value = description;
                opt.textContent = description;
                dataList.appendChild(opt);
            }
        });
    }
};

document.querySelector('#query').addEventListener('input', handleInput);