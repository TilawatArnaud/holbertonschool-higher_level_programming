#!/usr/bin/node
const { argv } = require('node:process');

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(argv[2]);
console.log(factorial(num));
