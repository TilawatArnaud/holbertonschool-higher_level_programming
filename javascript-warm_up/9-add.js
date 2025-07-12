#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  const add = a + b;
  console.log(add);
}
add(parseInt(argv[2]), parseInt(argv[3]));
