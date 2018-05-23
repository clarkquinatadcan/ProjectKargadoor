$(document).ready(function() {
    var bookingdata = getbookinglist(function(res){
      var d = new Date();
      $('#calendar').fullCalendar({
        header: {
          left: 'prev,next today',
          center: 'title',
          right: 'month,agendaWeek,agendaDay,listWeek'
        },
        defaultDate: d,
        navLinks: true, // can click day/week names to navigate views
        weekNumbers: true,
        weekNumbersWithinDays: true,
        weekNumberCalculation: 'ISO',
        editable: false,
        eventLimit: true, // allow "more" link when too many events
        events: res,
        // eventColor: '#378006'
      });
    });
  });
 
function getbookinglist(callback){
  var json = {};
  $.ajax({
      // async: false,
      type: 'GET', 
      url:'/api/booking/list',
      success: function(list){
        json = JSON.parse(list);
        callback(json);
      }
  });
}
