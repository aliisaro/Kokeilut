'use strict';
const year = prompt("Enter a year: ");
const intYear = parseInt(year);

if (year % 4 == 0) {
  if (year % 100 == 0 && year % 400 == 0) {
    document.querySelector('#target').innerHTML = year + " is a leap year.";
  } else if (year % 100 == 0 && year % 400 != 0) {
    document.querySelector('#target').innerHTML = year + " is not a leap year.";
  } else {
    document.querySelector('#target').innerHTML = year + " is a leap year.";
  }
} else {
  document.querySelector('#target').innerHTML = year + " is not a leap year.";
}