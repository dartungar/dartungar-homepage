$(document).ready(function() {

  $('form').submit(function() {
    alert('Да, хозяин!');
    return true
  });

});

function copyFunction(elementId) {
  var copyText = $(elementId);
  copyText.select();
  document.execCommand("copy");
  alert("Текст скопирован в буфер обмена!");
}