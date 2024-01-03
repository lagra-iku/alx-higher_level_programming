#!/usr/bin/node
/*  a script that prints all characters of a Star Wars movie */

const request = require('request');
const request2 = require('request');
const page = 'https://swapi.co/api/films/' + process.argv[2];

request(page, function (error, status, body) {
  if (error) {
    console.error(error);
  } else {
    const response = JSON.parse(body);
    response = response.characters;
    for (const elem of Object.values(response)) {
      request2(elem, function (e, s, b) {
        if (e) {
          console.error(e);
        } else {
          console.log(JSON.parse(b).name);
        }
      });
    }
  }
});
