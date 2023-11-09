'use strict';
const input = prompt("Give a number: ")
let number = parseInt(input)

let answer = "true"

if (number > 1) {
  for (let i = 2; i < number; i++) {
    if (number % i === 0) {
      answer = "false"
    }
  }
} else {
  answer = "false"
}


if (answer === "true") {
  document.querySelector('#target').innerHTML = number + " is a prime number";
} else {
  document.querySelector('#target').innerHTML = number + " is not a prime number";
}




