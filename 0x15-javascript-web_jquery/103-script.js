$(function () {
  function language (){
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
}
$('#btn_translate').click(language);
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      language();
    }
  });
});

