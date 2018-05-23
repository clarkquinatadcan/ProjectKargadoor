// UNAUTHORIZED PERSONNEL ONLY

(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.dropdown-trigger').dropdown();
      $('input#input_text, textarea#description').characterCounter();

    }); // end of document ready
  })(jQuery); // end of jQuery name space
  

$(document).ready(function () {
    $( "#formsub" ).click(function() {
        $( "#form" ).submit();
    });
});