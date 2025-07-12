#!/usr/bin/node
const { argv } = require('node:process');
const first = argv[2] || 'undefined';
const second = argv[3] || 'undefined';
console.log(`${first} is ${second}`);
