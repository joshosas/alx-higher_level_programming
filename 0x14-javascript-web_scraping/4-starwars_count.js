#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const charID = '18';
let count = 0;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(charID)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
