#!/usr/bin/node

const { dict } = require('./101-data');
const newdict = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (occurrences in newdict) {
    newdict[occurrences].push(parseInt(userId));
  } else {
    newdict[occurrences] = [parseInt(userId)];
  }
}

console.log(newdict);
