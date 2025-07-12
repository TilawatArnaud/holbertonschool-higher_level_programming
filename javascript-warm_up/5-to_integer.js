#!/usr/bin/node
const { argv } = require('node:process');
const firstArg = argv[2];
if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(firstArg)}`);
}
