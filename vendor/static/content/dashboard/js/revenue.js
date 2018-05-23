 //Revenue Line Chart
 var LineChartData = {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [ {
     label: "My Second dataset",
     fillColor: "rgba(151,187,205,0.2)",
     strokeColor: "rgba(151,187,205,1)",
     pointColor: "rgba(151,187,205,1)",
     pointStrokeColor: "#fff",
     pointHighlightFill: "#fff",
     pointHighlightStroke: "rgba(151,187,205,1)",
     data: [28, 48, 40, 19, 86, 27, 20, 27, 20, 27, 20, 27]
    }]
   };
   
  
   window.onload = function() {
  
    window.LineChartData = new Chart(document.getElementById("revenue-chart").getContext("2d")).Line(LineChartData,{
     responsive:true
    });
   };
   