


function process_htable(obj, dropdown_id) {
	var table_data = get_data_to_js('/query_data?table='.concat(obj.text));
	var settings1 = {
		data: table_data.slice(1),
		colHeaders: table_data[0],  
manualColumnResize: true, 
 autoWrapRow: true,
 // manualRowResize: true,
 //manualRowMove: true,
  manualColumnMove: true,
 // stretchH: "all",
		licenseKey: 'non-commercial-and-evaluation'
	}

 document.getElementById('button_drp_id_1').innerHTML=obj.text;
	var handsome_container = document.getElementById('h_table_id'),
	hot2;
	handsome_container.innerHTML = ""
	hot2 = new Handsontable(handsome_container, settings1);
dropdown_show(dropdown_id);



	

}

