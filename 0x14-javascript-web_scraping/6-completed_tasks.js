#!/usr/bin/node
/* a script that computes the number of tasks completed by user id */

const request = require('request');
const page = process.argv[2];
const newdict = {};

request(page, function (error, status, body) {
  if (error) {
    console.error(error);
  } else {
    const response = JSON.parse(body);
    for (const task of Object.values(response)) {
      if (task.completed) {
        if (newdict[task.userId]) {
          newdict[task.userId] += 1;
        } else {
          newdict[task.userId] = 1;
        }
      }
    }
    console.log(newdict);
  }
});
