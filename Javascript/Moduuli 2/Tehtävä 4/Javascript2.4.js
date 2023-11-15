'use strict';
let list = []

let number = prompt("Give a number:")
let int = parseInt(number)
list.push(int)

while (int !== 0) {
  number = prompt("Give a number:")
  int = parseInt(number)
  list.push(int)
}
list.sort(function(a, b){return b-a});

for (let i = 0; i < list.length; i++) {
  console.log(list[i])
}