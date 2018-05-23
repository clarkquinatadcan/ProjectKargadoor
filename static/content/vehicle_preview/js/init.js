(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.dropdown-trigger').dropdown();
      $("#reply-btn").click(function() {
          $("#replybox-form").show();
      });
      
    }); // end of document ready
  })(jQuery); // end of jQuery name space
  