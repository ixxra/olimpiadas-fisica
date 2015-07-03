#!/usr/bin/env node
/*
USAGE:
  reverseSort.json <path/to/json>
Sorts olympiads from latest to earliest. Prints results to stdout
*/
var fs = require('fs');
var target = process.argv[2];

var meta = JSON.parse(fs.readFileSync(target).toString());

var olympiads = meta.olympiads;
olympiads.forEach(function castYear(o) {
  o.year = Number(o.year);
});

olympiads.reverse();
console.log(JSON.stringify(meta));
