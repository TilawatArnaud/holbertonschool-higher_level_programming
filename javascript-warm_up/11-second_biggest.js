#!/usr/bin/node
const { argv } = require('node:process');

const args = argv.slice(2).map(arg => parseInt(arg));

if (args.length <= 1) {
  console.log(0);
  process.exit(0);
}

const sortedUnique = [...new Set(args)].sort((a, b) => b - a);

const secondBiggest = sortedUnique.length > 1 ? sortedUnique[1] : 0;

console.log(secondBiggest);
