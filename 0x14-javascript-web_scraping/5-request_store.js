#!/usr/bin/node

/* a script that gets the contents of a webpage and stores it in a file. */

const request = require('request');
const fs = require('fs');
const webpage = process.argv[2];
const file = process.argv[3];

request(webpage, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFileSync(file, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
