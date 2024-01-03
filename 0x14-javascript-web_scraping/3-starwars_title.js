#!/usr/bin/node
/* a script that display the status code of a GET request. */
const request = require('request');

const movieID = process.argv[2];
const starwar = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

request(starwar, function (error, status, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
