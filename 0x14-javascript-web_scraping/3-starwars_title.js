#!/usr/bin/node
const request = require('request');
let url = 'http://swapi.co/api/films/';
let episode = process.argv[2];
request(url + episode, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    let jsonObj = JSON.parse(body);
    console.log(jsonObj.title);
  } else {
    console.log('An error occured. Status code: ' + res.statusCode);
  }
});
