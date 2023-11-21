'use strict';
let lista = []
function even(all) {
  for (let i = 0; i < all.length; i++) {
    if (all[i] % 2 === 0) {
      lista.push(all[i])
    }
  }
}

const numbers = [2, 7, 4];
even.apply(numbers);

document.querySelector('#target1').innerHTML = numbers;
document.querySelector('#target2').innerHTML = lista;