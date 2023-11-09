'use strict';
const year = prompt("Enter a year: ");
const intYear = parseInt(year);

if (intYear % 4 == 0) {
  if (intYear % 100 == 0 && intYear % 400 == 0) {
    document.querySelector('#target').innerHTML = year + " is a leap year.";
  } else if (intYear % 100 == 0 && intYear % 400 != 0) {
    document.querySelector('#target').innerHTML = year + " is not a leap year.";
  } else {
    document.querySelector('#target').innerHTML = year + " is a leap year.";
  }
} else {
  document.querySelector('#target').innerHTML = year + " is not a leap year.";
}