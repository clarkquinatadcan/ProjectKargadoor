// UNAUTHORIZED PERSONNEL ONLY

(function($){
    $(function(){
      $('select').formSelect();
      $('.sidenav').sidenav();
      $('.dropdown-trigger').dropdown();
      $('input#input_text, textarea#description').characterCounter();

        // Basic image upload
        $('.dropify').dropify();

        // Translated
        // $('.dropify-fr').dropify({
        //     messages: {
        //         default: 'Glissez-déposez un fichier ici ou cliquez',
        //         replace: 'Glissez-déposez un fichier ou cliquez pour remplacer',
        //         remove:  'Supprimer',
        //         error:   'Désolé, le fichier trop volumineux'
        //     }
        // });

        // Used events

        // });    // Multiple images preview in browser

        // var imagesPreview = function(input, placeToInsertImagePreview) {

        //     if (input.files) {
        //         var filesAmount = input.files.length;

        //         for (i = 0; i < filesAmount; i++) {
        //             var reader = new FileReader();

        //             reader.onload = function(event) {
        //                 $($.parseHTML('<img>')).attr('src', event.target.result).appendTo(placeToInsertImagePreview);
        //                 $($.parseHTML('<input name="images" hidden>')).attr('value', event.target.result).appendTo(placeToInsertImagePreview);
        //             }

        //             reader.readAsDataURL(input.files[i]);
        //         }
        //     }

        // };

        // $('#gallery-photo-add').on('change', function() {
        //     imagesPreview(this, 'li.truck-thumb');
        // });


        if (window.File && window.FileList && window.FileReader) {
            $("#files").on("change", function(e) {
              var files = e.target.files,
                filesLength = files.length;
              for (var i = 0; i < filesLength; i++) {
                var f = files[i]
                var fileReader = new FileReader();
                fileReader.onload = (function(e) {
                  var file = e.target;
                  $("<span class=\"pip\">" +
                    "<img class=\"imageThumb\" src=\"" + e.target.result + "\" title=\"" + file.name + "\"/>" +
                    "<br/><span class=\"remove\">Remove image</span>" +
                    "</span>" + "<input name=\"images\" value=\"" + e.target.result + "\" hidden>").insertAfter("#files");
                //   $($.parseHTML('<input name="images" hidden>')).attr('value', e.target.result)
                  $(".remove").click(function(){
                    $(this).parent(".pip").remove();
                  });
                  
                });
                fileReader.readAsDataURL(f);
              }
            });
          } else {
            alert("Your browser doesn't support to File API")
          }


    }); // end of document ready
  })(jQuery); // end of jQuery name space
  

  // $(document).ready(function () {
  //   $( "#formsub" ).click(function() {
  //       $( "#form" ).submit();
  //   });
  // });



  $(function() {
    $("#enviar").click(function (event) {
        
        if ($("#files").val() && $("#hey").val() && $("#platenumber").val() 
            && $("#qty").val() && $("#capacity").val() 
            && $("#price").val() && $("#stockonhand").val() 
            && $("#unit").val() && $("#tankcapacity").val() 
            && $("#description").val() ) 
        {
            var n = swal({
                title: "Vehicle Add Successfully!.",
                text: "But need an approval to the admin.",
                type: "success", 
                allowOutsideClick: false,
                timer:7000,
            }, function(){
                    form.submit();
                });
        }
        else {
            swal({
            title: "Warning",
            text: "There are some fields need to fill out.",
            type: "warning", 
            allowOutsideClick: false,
            timer:5000,
            });
        }
        
    });
});