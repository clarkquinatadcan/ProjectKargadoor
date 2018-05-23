(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.dropdown-trigger').dropdown();

    }); // end of document ready
  })(jQuery); // end of jQuery name space
  

  $(document).ready(function () {
    $( "#formsub" ).click(function() {
        
        $( "#form" ).submit();
    });
    $("#form").change(function(){
      var address = $("#addrss").val();
      if(address !="") {
        var d = $("#addrss").val();
        var res = d.replace(/ /g, "+"); 
        var url="https://maps.googleapis.com/maps/api/geocode/json?address="+res+"&key=AIzaSyDQJXnGwZhNT-NktU4pwmKlUpDvL2rlCqw";

        $.getJSON(url, function (json) { // Set the variables from the results array var address = json.results[0].formatted_address;
            // console.log('Address : ', address); 
            var latitude = json.results[0].geometry.location.lat; console.log('Latitude : ', latitude);
            var longitude = json.results[0].geometry.location.lng; console.log('Longitude : ', longitude); 
            var place_id=json.results[0].place_id;
            $("#lat").val(latitude);
            $("#lon").val(longitude);
            console.log(place_id); 
            console.log('Latitude : ', latitude); 
            console.log('longitude : ', longitude); 
            console.log('json value:', json.results);
            // initMap(latitude,longitude,place_id,jo); 
            }
        ); 
      }
      
    });
  });