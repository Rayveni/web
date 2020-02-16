

$('#start_date').daterangepicker({
    "singleDatePicker": true,
	"showWeekNumbers": true,
    "autoApply": true,
"locale": {
"format": "YYYY-MM-DD"
}
,
    "startDate": today(3),

}, function(start, end, label) {
  console.log("New date range selected: ' + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD') + ' (predefined range: ' + label + ')");
});

$('#end_date').daterangepicker({
    "singleDatePicker": true,
	"showWeekNumbers": true,
    "autoApply": true,
   
"locale": {
"format": "YYYY-MM-DD"
}
,
    "startDate": today(6)

}, function(start, end, label) {
  console.log("New date range selected: ' + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD') + ' (predefined range: ' + label + ')");
});

function myFunction() {
  alert(123);
}
;