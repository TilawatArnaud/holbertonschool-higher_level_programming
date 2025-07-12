#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.slice(2);
const i = parseInt(args[0]);

if (args.length === 0 || isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < i; j++) {
    console.log('C is fun');
  }
}
