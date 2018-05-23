(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.dropdown-trigger').dropdown();
      $('.slider').slider();
      $('select').formSelect();
      $('.modal').modal();
      $('.settings').click(function(){
            $('.choices').slideToggle("slow");
      });


    }); // end of document ready
  })(jQuery); // end of jQuery name space
  