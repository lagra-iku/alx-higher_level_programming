#!/usr/bin/node
/* a script that writes to a file */

const fs = require('fs');

const filePath = process.argv[2];
const inputstring = process.argv[3];

fs.writeFile(filePath, inputstring, (err) => {
  if (err) {
    console.error(err);
  }
});
