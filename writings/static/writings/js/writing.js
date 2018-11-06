
var index = 0;
var int = setInterval(function(){
  var $paper = $('.paper').eq(index);
  if($paper.length)
  {
    $paper.addClass('grow');
    index++;
  }
  else
  {
    clearInterval(int);
  } 
}, 50);

setTimeout(function(){
  $('.message').addClass('fade-out');
}, 2000);