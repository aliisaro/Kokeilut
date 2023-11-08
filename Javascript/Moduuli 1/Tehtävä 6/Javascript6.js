'use strict';
const answer = confirm("Should I calculate the square root?");

if (answer == true) {
  const number = prompt("Please give a number: ");
  const intNumber = parseInt(number);

  if (intNumber > 0) {
    const square = Math.sqrt(intNumber);
    document.querySelector('#target').innerHTML = "The square root of " + intNumber + " is " + square + ".";
  } else {
    document.querySelector('#target').innerHTML = "The square root of a negative number is not defined.";
  }

} else {
  document.querySelector('#target').innerHTML = "The square root is not calculated.";
}
