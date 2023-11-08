'use strict';
const name = prompt("Your name: ");
const number = Math.floor(Math.random() * 5);

if (number == 1) {
  document.querySelector('#target').innerHTML = name + ", you are a Hufflepuff";
} else if (number == 2) {
  document.querySelector('#target').innerHTML = name + ", you are a Ravenclaw";
} else if (number == 3) {
  document.querySelector('#target').innerHTML = name + ", you are a Gryffindor";
} else if (number == 4) {
  document.querySelector('#target').innerHTML = name + ", you are a Slytherin";
}