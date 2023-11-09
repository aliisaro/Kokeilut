'use strict';
const year1 = prompt("Enter a start year: ");
const year2 = prompt("Enter a end year: ");

let start = parseInt(year1);
const end = parseInt(year2);

let leapyears = []

while (start != end) {
  if ((0 == start % 4) && (0 != start % 100) || (0 == start % 400)) {
    leapyears.push(start)
  }
  start = start + 1
}


let list = document.getElementById("myList");
for (let i = 0; i < leapyears.length; ++i) {
    let li = document.createElement('li');
    li.innerText = leapyears[i];
    list.appendChild(li);
}