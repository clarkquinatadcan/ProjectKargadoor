// *
// * Add multiple markers
// * 2013 - en.marnoto.com
// *

// necessary variables
var map;
var infoWindow;

// markersData variable stores the information necessary to each marker
var markersData = [
   {
      lat: 10.3295046,
      lng: 123.9279495,
      name: "Urban Homes Building 18",
      address1:"Mandaue City",
      address2: "CodeChiq",
      postalCode: "3830-772" // don't insert comma in the last item of each marker
   },
   {
      lat: 10.3242078,
      lng: 123.9224083,
      name: "Wireless Subangdaku Vendor's Association Inc.",
      address1:"Mandaue City",
      address2: "Cebu",
      postalCode: "3830-453" // don't insert comma in the last item of each marker
   },
   {
      lat: 10.3240178,
      lng: 123.9173013,
      name: "RainForest Park Cebu",
      address1:"F. Cabahug St, TELO Square, Cebu City, 6000 Cebu",
      address2: "Mandaue City",
      postalCode: "3830-453" // don't insert comma in the last item of each marker
   },
   {
      lat: 10.322519,
      lng: 123.913042,
      name: "Castle Peak Hotel",
      address1:"Lungsod ng Cebu, Lalawigan ng Cebu",
      address2: "Cebu City, Cebu",
      postalCode: "3830-225" // don't insert comma in the last item of each marker
   } // don't insert comma in the last item
];


function initialize() {
   var mapOptions = {
      center: new google.maps.LatLng(10.3295481,123.927922),
      zoom: 9,
      mapTypeId: 'roadmap',
   };

   map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

   // a new Info Window is created
   infoWindow = new google.maps.InfoWindow();

   // Event that closes the Info Window with a click on the map
   google.maps.event.addListener(map, 'click', function() {
      infoWindow.close();
   });

   // Finally displayMarkers() function is called to begin the markers creation
   displayMarkers();
}
google.maps.event.addDomListener(window, 'load', initialize);


// This function will iterate over markersData array
// creating markers with createMarker function
function displayMarkers(){

   // this variable sets the map bounds according to markers position
   var bounds = new google.maps.LatLngBounds();
   
   // for loop traverses markersData array calling createMarker function for each marker 
   for (var i = 0; i < markersData.length; i++){

      var latlng = new google.maps.LatLng(markersData[i].lat, markersData[i].lng);
      var name = markersData[i].name;
      var address1 = markersData[i].address1;
      var address2 = markersData[i].address2;
      var postalCode = markersData[i].postalCode;

      createMarker(latlng, name, address1, address2, postalCode);

      // marker position is added to bounds variable
      bounds.extend(latlng);  
   }

   // Finally the bounds variable is used to set the map bounds
   // with fitBounds() function
   map.fitBounds(bounds);
}

// This function creates each marker and it sets their Info Window content
function createMarker(latlng, name, address1, address2, postalCode){
   var image = 'https://i.imgur.com/k26gNsf.png';
   var marker = new google.maps.Marker({
      map: map,
      position: latlng,
      title: name,
      animation: google.maps.Animation.DROP,
      icon: image
   });

   // This event expects a click on a marker
   // When this event is fired the Info Window content is created
   // and the Info Window is opened.
   google.maps.event.addListener(marker, 'click', function() {
      
      // Creating the content to be inserted in the infowindow
      var iwContent = '<div id="iw_container">' +
            '<div class="iw_title">' + name + '</div>' +
         '<div class="iw_content">' + address1 + '<br />' +
         address2 + '<br />' +
         postalCode + '</div></div>';
      
      // including content to the Info Window.
      infoWindow.setContent(iwContent);

      // opening the Info Window in the current map and at the current marker location.
      infoWindow.open(map, marker);
   });
}


