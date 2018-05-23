// (function($){
//   $(function(){

//     $('.sidenav').sidenav();
//     $('.dropdown-trigger').dropdown();

//   }); // end of document ready
// })(jQuery); // end of jQuery name space

// // MAP RADIUS AND HEATMAP
// var citymap = {
//   tipolo: {
//       center: {lat: 10.3283848, lng: 123.9270473},
//       capacity_radius: 2
//   },
//   cebu: {
//       center: {lat: 10.3141261, lng: 123.9127306},
//       capacity_radius: 8
//   },
//   banilad: {
//       center: {lat: 10.3371026, lng: 123.9134764},
//       capacity_radius: 5
//   },

// };

// var map, heatmap;
// function initMap() {
//   // Create the map.
//   map = new google.maps.Map(document.getElementById('map'), {
//       zoom: 17,
//       center: {lat: 10.3276843, lng: 123.9222363},
//       mapTypeId: 'satellite'
//   });

//   heatmap = new google.maps.visualization.HeatmapLayer({
//       data: getPoints(),
//       map: map
//   });
//   // Construct the circle for each value in citymap.
//   // Note: We scale the area of the circle based on the population.
//   for (var city in citymap) {
//   // Add the circle for this city to the map.
//   var cityCircle = new google.maps.Circle({
//       strokeColor: '#FF0000',
//       strokeOpacity: 0.8,
//       strokeWeight: 2,
//       fillColor: '#FF0000',
//       fillOpacity: 0.35,
//       map: map,
//       center: citymap[city].center,
//       radius: Math.sqrt(citymap[city].capacity_radius) * 100
//   });
//   }
// }


// function toggleHeatmap() {
//     heatmap.setMap(heatmap.getMap() ? null : map);
// }

// function changeGradient() {
//     var gradient = [
//       'rgba(0, 255, 255, 0)',
//       'rgba(0, 255, 255, 1)',
//       'rgba(0, 191, 255, 1)',
//       'rgba(0, 127, 255, 1)',
//       'rgba(0, 63, 255, 1)',
//       'rgba(0, 0, 255, 1)',
//       'rgba(0, 0, 223, 1)',
//       'rgba(0, 0, 191, 1)',
//       'rgba(0, 0, 159, 1)',
//       'rgba(0, 0, 127, 1)',
//       'rgba(63, 0, 91, 1)',
//       'rgba(127, 0, 63, 1)',
//       'rgba(191, 0, 31, 1)',
//       'rgba(255, 0, 0, 1)'
//     ]
//     heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
// }

// function changeRadius() {
//     heatmap.set('radius', heatmap.get('radius') ? null : 20);
// }

// function changeOpacity() {
//     heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
// }

// // Heatmap data: 500 Points
// function getPoints() {
//     return [
//         new google.maps.LatLng(10.3216843, 123.9210063),           
//         new google.maps.LatLng(10.3226843, 123.9210363),           
//         new google.maps.LatLng(10.3236843, 123.9211363),           
//         new google.maps.LatLng(10.3246843, 123.9212563),           
//         new google.maps.LatLng(10.3276843, 123.9222363),           
//         new google.maps.LatLng(10.3277512, 123.9232541),           
//         new google.maps.LatLng(10.3277901, 123.9245585),           
//         new google.maps.LatLng(10.3278524, 123.9245284),           
//         new google.maps.LatLng(10.3278242, 123.9246852),           
//         new google.maps.LatLng(10.3279552, 123.9250212),           
//         new google.maps.LatLng(10.3282701, 123.9272522),           
//         new google.maps.LatLng(10.3289701, 123.9282522),           
//         new google.maps.LatLng(10.3299701, 123.9292522),           
//     ];
// }


(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.dropdown-trigger').dropdown();
  
    }); // end of document ready
  })(jQuery); // end of jQuery name space
  