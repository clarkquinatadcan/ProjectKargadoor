(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.dropdown-trigger').dropdown();
      $('.scrollspy').scrollSpy();
      $('select').formSelect();
      $('.tabs').tabs();
      $('.modal').modal({
          dismissible: false
      });

    }); // end of document ready
  })(jQuery); // end of jQuery name space
  