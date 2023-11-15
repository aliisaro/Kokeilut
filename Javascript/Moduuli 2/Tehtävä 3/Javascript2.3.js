'use strict';
let count = 1
let list = []

while (6 >= count) {
  let name = prompt("Give a name of doggie " + count + ":")
  list.push(name)
  count = count + 1
}

list.sort();
list.reverse()

let newlist = document.getElementById("myList");
for (let i = 0; i < list.length; ++i) {
    let li = document.createElement('li');
    li.innerText = list[i];
    newlist.appendChild(li);
}