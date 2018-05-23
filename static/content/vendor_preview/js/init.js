(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.dropdown-trigger').dropdown();
    $('select').formSelect();

  }); // end of document ready
})(jQuery); // end of jQuery name space

/*Show entries on click hide*/
$(document).ready(function(){
  $(".dropdown-content.select-dropdown li").on( "click", function() {
      var that = this;
      setTimeout(function(){
      if($(that).parent().hasClass('active')){
              $(that).parent().removeClass('active');
              $(that).parent().hide();
      }
      },100);
  });
});