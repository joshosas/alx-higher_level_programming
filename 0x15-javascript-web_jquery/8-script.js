$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
    if (status === 'success') {
      let films = data.results;
      for (let film in films) {
        $('#list_movies').append('<li>' + film.title + '</li>');
      }
    }
  });
});

