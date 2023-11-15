'use strict';
function concat(a, b, c) {
  const sentence = "".concat(a, b, c);
  document.querySelector('#target').innerHTML = sentence;
}

const list = ["Moi, ", "mitä ", "kuuluu?"];
concat.apply(null, list);