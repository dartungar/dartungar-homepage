function copyToClipboard(element) {
  var $temp = $("<input>");
  $("body").append($temp);
  $temp.val($(element).text()).select();
  document.execCommand("copy");
  $temp.remove();
}

function copyFunction(element_id) {
  var copyText = document.getElementById(element_id);
  copyText.select();
  document.execCommand("Copy");
  alert("Текст скопирован в буфер обмена!");
}
