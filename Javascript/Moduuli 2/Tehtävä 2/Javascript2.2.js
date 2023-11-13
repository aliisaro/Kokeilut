'use strict';
let number = prompt("Give a number of participants:")
let count = parseInt(number)
let list = []

while (0 < count) {
  let name = prompt("Give a name:")
  list.push(name)
  count = count - 1
}

let ordered = list.sort();

let newlist = document.getElementById("myList");
for (let i = 0; i < ordered.length; ++i) {
    let li = document.createElement('li');
    li.innerText = list[i];
    newlist.appendChild(li);
}