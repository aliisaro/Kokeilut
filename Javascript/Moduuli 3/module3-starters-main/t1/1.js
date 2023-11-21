'use strict';

const div = document.querySelector("#target");
const html =
    `<li>First item</li>
    <li>Second item</li>
    <li>Third item</li>`;
div.innerHTML = html;

document.getElementById("target").classList.add("my-list")