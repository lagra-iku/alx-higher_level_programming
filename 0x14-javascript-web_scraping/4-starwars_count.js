#!/usr/bin/node
/* a script that display the status code of a GET request. */
const request = require('request');

const apiURL = process.argv[2];

request(apiURL, function (error, status, body) {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body).results;

  const wedgeMovies = films.filter((film) =>
    film.characters.some((characterUrl) => characterUrl.includes('18'))
  );

  console.log(wedgeMovies.length);
});
