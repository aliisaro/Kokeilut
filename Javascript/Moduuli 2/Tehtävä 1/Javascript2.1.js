'use strict';
const input1 = prompt("Give a number: ")
const input2 = prompt("Give another number: ")
const input3 = prompt("Another number: ")
const input4 = prompt("Another one: ")
const input5 = prompt("Give the last number: ")

let n1 = parseInt(input1)
let n2 = parseInt(input2)
let n3 = parseInt(input3)
let n4 = parseInt(input4)
let n5 = parseInt(input5)

let list = []

list.push(n5)
list.push(n4)
list.push(n3)
list.push(n2)
list.push(n1)

for (let i in list) {
  console.log(list[i])
}