'use strict';
let int = "0"
let list = []
let sameElement = list.includes(int)

while (sameElement === false) {

    let number = prompt("Give a number:")
    int = parseInt(number)
    sameElement = list.includes(int)
    list.push(int)
}

console.log("Number is already in list.")
list.sort((a, b) => a - b);

for (let i = 0; i < list.length; i++) {
  console.log(list[i])
}