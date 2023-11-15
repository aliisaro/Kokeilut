'use strict';
let list = []
let lastElement = list[list.length - 1];

function dice() {
  let random= Math.floor(Math.random() * 7);
  list.push(random)
  lastElement = list[list.length - 1];
}

while (lastElement !== 6) {
  dice();
}

let newlist = document.getElementById("Mylist");
for (let i = 0; i < list.length; ++i) {
    let li = document.createElement('li');
    li.innerText = list[i];
    newlist.appendChild(li);
}