'use strict';

let prevQuery = '';

const handleInput = (evt) => {
    const query = evt.target.value;
    const diffLength = prevQuery.length - query.length;

    if (query.length !== 0 && (diffLength === 1 || diffLength === -1)) {
        
        const queryString = new URLSearchParams({ query }).toString();
        
        fetch(`/autocomplete.json?${queryString}`)
        .then((response) => response.json())
        .then((resultsArray) => {
            // console.log(resultsArray);
            
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

    prevQuery = query;
};

document.querySelector('#query').addEventListener('input', handleInput);