$(function () {
  $('#btn_translate').click(function () {
    $.get('https://www.fourtonfish.com/hellosalut/hello/', function (data, status) {
      if (status === 'success' && data !== null) {
        $content_text = $('#language_code').text();
        if (data.code === $content_text) {
          $('#hello').text(data.hello)
        }
      }
    });
  });
});

