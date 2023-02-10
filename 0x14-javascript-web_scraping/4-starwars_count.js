#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const films = JSON.parse(body).results;
  const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';
  let count = 0;
  for (const movie of films) {
    if (movie.characters.includes(wedgeAntilles)) count++;
  }
  console.log(count);
});
