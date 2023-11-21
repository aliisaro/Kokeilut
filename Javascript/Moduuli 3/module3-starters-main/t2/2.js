'use strict';
let list = document.getElementById("target");

let li = document.createElement('li');
li.innerText = "First item";
list.appendChild(li);

li = document.createElement('li');
li.innerText = "Second item";
list.appendChild(li);

li = document.createElement('li');
li.innerText = "Third item";
list.appendChild(li);

document.getElementsByTagName("li")[1].classList.add("my-list");