'use strict';

const currentRoute = window.location.pathname;

const currentLink = document.querySelector(`a[href="${currentRoute}"]`);
currentLink.classList.add('active');
currentLink.setAttribute('aria-current', 'page');
