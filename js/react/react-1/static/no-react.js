const clickButton = document.getElementById('click-button');

clickButton.addEventListener('click', (evt) => {
  evt.target;
  const countElement = document.getElementById('click-count');
  countElement.innerText = Number(countElement.innerText) + 1;
});
