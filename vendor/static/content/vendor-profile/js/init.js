
function myMap() {
    var mapOptions = {
        center: new google.maps.LatLng(10.261799, 123.836048),
        zoom: 17,
        mapTypeId: google.maps.MapTypeId.HYBRID
    }
var map = new google.maps.Map(document.getElementById("map"), mapOptions);
}
