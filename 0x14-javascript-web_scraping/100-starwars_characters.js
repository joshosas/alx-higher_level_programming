#!/usr/bin/node
const request = require('request');
const film = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/people/';
function filmcharacters (film, url) {
  request(url, (err, res, body) => {
    if (err) {
      console.log(err);
    } else if (res.statusCode === 200) {
      const jsonobj = JSON.parse(body);
      const people = jsonobj.results;
      for (const i in people) {
        for (const j in people[i].films) {
          if (people[i].films[j].includes(film)) {
            console.log(people[i].name);
          }
        }
      }
      if (jsonobj.next !== null) {
        filmcharacters(film, jsonobj.next);
      }
    } else {
      console.log('An error occured. Status code: ' + res.statusCode);
    }
  });
}
filmcharacters(film, url);
