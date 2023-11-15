'use strict';
let list = []
let lastElement = list[list.length - 1];

let sides = prompt("Give a number of sides for the dice:")
let intSides = parseInt(sides)
function dice(number) {
  let random= Math.floor(Math.random() * (number + 1));
  list.push(random)
  lastElement = list[list.length - 1];
}

while (lastElement !== intSides) {
  dice(intSides);
}

let newlist = document.getElementById("Mylist");
for (let i = 0; i < list.length; ++i) {
    let li = document.createElement('li');
    li.innerText = list[i];
    newlist.appendChild(li);
}