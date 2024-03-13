// Pick a secret number
const myNumber = Math.floor(Math.random() * 100);

// Guess the number 50
let guess = 50;

if (guess < myNumber) {
  console.log('Too low!');
} else if (guess > myNumber) {
  console.log('Too high!');
} else {
  console.log('Yay!');
}