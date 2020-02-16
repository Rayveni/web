

function today(add_month=0) {
	var today_var = new Date();
	if (add_month>0) {
	  today_var.setMonth(today_var.getMonth() + add_month);
	}
var dd = String(today_var.getDate()).padStart(2, '0');
var mm = String(today_var.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today_var.getFullYear();

return yyyy  + '-' + mm + '-' + dd;
}

(function($) {
  "use strict"; // Start of use strict

  // Toggle the side navigation
  $("#sidebarToggle, #sidebarToggleTop").on('click', function(e) {
    $("body").toggleClass("sidebar-toggled");
    $(".sidebar").toggleClass("toggled");
    if ($(".sidebar").hasClass("toggled")) {
      $('.sidebar .collapse').collapse('hide');
    };
  });




})(jQuery); // End of use strict



