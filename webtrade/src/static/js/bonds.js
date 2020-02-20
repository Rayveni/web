

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


function crossfilter_coverter(table_name) {
	data_arr=get_data_to_js('/query_data?table='+table_name)
	
    return {
        columns: data_arr[0],
        data: crossfilter(data_arr.slice(1)),
    };
};

var rubonds = crossfilter_coverter('smartlabbondsrus');

var eurbonds = crossfilter_coverter('smartlabbondsusd');
var handsome_container = document.getElementById('h_table_id');

function bonds_filter(bonds_cf,bond_category) {
	bond_cat_index=bonds_cf.columns.indexOf("bond_category")
	
	var topicsDim = bonds_cf.data.dimension(function(d){ return d[bond_cat_index];});
	
	topicsDim .filter(function(d) {return d ==bond_category})
	
	var filtered_data=topicsDim.top(Infinity);
	topicsDim.filterAll();
    return {
        columns: bonds_cf.columns,
        data: filtered_data,
    };
};

function exclude_columns(data_columns) {
	exclude_list=['bond_category',"last_deal","sys_updated","years_till_redemption",]
	return exclude_list.map(_column => data_columns.indexOf(_column));
};
function process_htable(table_data) {

    var settings1 = {
        data: table_data.data,
        colHeaders: table_data.columns,
        manualColumnResize: true,
        autoWrapRow: true,
	
		
		 hiddenColumns: {
    columns: exclude_columns(table_data.columns),
   // indicators: true
  },
        // manualRowResize: true,
        //manualRowMove: true,
        manualColumnMove: true,
        // stretchH: "all",
        licenseKey: 'non-commercial-and-evaluation'
    }

    handsome_container.innerHTML = ""
    var hot2 = new Handsontable(handsome_container, settings1);

};



function draw_hs_table(bond_category) {
	if (bond_category=='ЕВРО') {
  process_htable({columns: eurbonds.columns,data: eurbonds.data.all()});
} else {
  process_htable(bonds_filter(rubonds,bond_category));
}
		

};