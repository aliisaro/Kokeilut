'use strict';
let amount = prompt("Give a number: ");
let intAmount = parseInt(amount);

const numbers = []

while (intAmount > 0) {
  let number = Math.floor(Math.random() * 7);
  console.log(number);
  numbers.push(number);
  intAmount -= 1;
}

console.log(numbers)

let sum = 0;
for (let i of numbers) {
  sum = sum + i;
}

document.querySelector('#target').innerHTML = "The sum of the results is " + sum;