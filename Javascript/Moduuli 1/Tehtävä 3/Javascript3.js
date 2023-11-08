'use strict';
const first = prompt("Give a number:");
const second = prompt("Give a another number:");
const third = prompt("Give a third number:");

const firstInt = parseInt(first);
const secondInt = parseInt(second);
const thirdInt = parseInt(third);

const sum = firstInt + secondInt + thirdInt;
const product = firstInt * secondInt * thirdInt;
const average = sum / 3;

document.querySelector('#target').innerHTML = "The sum: " + sum + ". The product: " + product + ". The average: " + average.toFixed(1) + ".";
