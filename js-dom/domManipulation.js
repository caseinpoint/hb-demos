/* namespace */

// console.log(msg);


/* dialogs */

// alert('Message to pop up');

// const confirmed = confirm('Hey, user, is this ok?');
// console.log(`Confirmed? ${confirmed}`);

// let promptAnswer = prompt('Enter a string');
// console.log(`Entered in "${promptAnswer}"`);

// while (!promptAnswer) {
//     promptAnswer = prompt('Enter a string');
//     console.log(`Entered in "${promptAnswer}"`);
// }


/* querySelector */

const firstPTag = document.querySelector('p.lead');
// console.log('firstPTag', firstPTag);

const mainContent = document.querySelector('#main-content');
// console.log('mainContent', mainContent);


/* querySelectorAll */

const paragraphs = document.querySelectorAll('p');
// console.log('paragraphs', paragraphs);


/* manipulating the DOM */

const aboutLink = document.querySelector('a');
// console.log(`aboutLink.innerHTML: ${aboutLink.innerHTML}`);
aboutLink.innerHTML = 'About Me';

// mainContent.innerHTML = 'Something else';

const catPhoto = document.querySelector('img');
// catPhoto.setAttribute('src', 'cat2.gif');
// console.log('catPhoto', catPhoto);
catPhoto.src = 'cat2.gif';
// console.log('catPhoto src', catPhoto.getAttribute('src'));


/* classList */

const blogContainer = document.querySelector('div');
// remember: first div
// console.log('blogContainer.classList', blogContainer.classList);
// blogContainer.classList.remove('blog-content');
// blogContainer.classList.add('article');

// document.querySelector('#main-content').classList.add('fancy');
// mainContent.classList.add('fancy');
// console.log('contains fancy?',
//     mainContent.classList.contains('fancy'));
// mainContent.classList.remove('fancy');
// console.log('contains fancy?',
//     mainContent.classList.contains('fancy'));

for (const p of paragraphs) {
  p.classList.add('fancy');
}


/* insertAdjacentHTML */

const firstUL = document.querySelector('ul');
firstUL.insertAdjacentHTML('afterbegin',
    '<li>Learn about the DOM</li>');
firstUL.insertAdjacentHTML('beforeend',
    '<li>Finish homework</li>');


/* remove */

// firstUL.remove();
// while (firstUL.firstChild) {
//     firstUL.firstChild.remove();
// }
for (const li of firstUL.children) {
    if (li.innerHTML === 'Finish homework') {
        console.log(li);
        li.remove();
    }
}


/* show/hide */

catPhoto.style.display = 'none';
catPhoto.style.display = '';


/* function (preview) */

function makeEverythingBlue() {
    const allH1Tags = document.querySelectorAll('h1');
    for (const hTag of allH1Tags) {
        hTag.style.color = 'blue';
    }

    const allPTags = document.querySelectorAll('p');
    for (const pTag of allPTags) {
        pTag.style.color = 'blue';
    }

    const allLiTags = document.querySelectorAll('li');
    for (const liTag of allLiTags) {
        liTag.style.color = 'blue';
    }

    const bdy = document.querySelector('body');
    bdy.classList.add('dark-background');
}
