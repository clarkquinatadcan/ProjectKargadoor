(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.dropdown-trigger').dropdown();

      // FORMAT NUMPAD
      $('#phone-demo').formatter({
          'pattern': '({{999}}) {{999}}-{{9999}}',
          'persistent': true
      });
      $('#phone-code').formatter({
          'pattern': '+63 {{999}}-{{999}}-{{9999}}',
          'persistent': true
      });


    }); // end of document ready
})(jQuery); // end of jQuery name space
  

$(function() {
    $("#addven").click(function (event) {
        
        if ($("#fname").val() && $("#lname").val() 
            && $("#address").val() && $("#email").val() 
            && $("#password").val() == $("#confirm_password").val() 
            && $("#phone-demo").val() && $("#phone-code").val() 
            && $("#payment").val() && $("#company-name").val() ) 
        {
            var n = swal({
                title: "New Vendor Add Successfully!.",
                text: "But need an approval to the admin.",
                type: "success", 
                allowOutsideClick: false,
                timer:10000,
            }, function(){
                    form.submit();
                });
        }
       
    });
});
