var  hot2;

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

    document.getElementById('button_drp_id_1').innerHTML = obj.text;
    var handsome_container = document.getElementById('h_table_id');

    handsome_container.innerHTML = ""
        hot2 = new Handsontable(handsome_container, settings1);
    dropdown_show(dropdown_id);

}

function drop_db_table(obj, dropdown_id) {
if (confirm("drop "+obj.text +"?")) {

$.post( "/upload_mongo_form", {
   'submit_button':'drop_table','table':obj.text
}); 
} ;


dropdown_show(dropdown_id);


}

function function_export_csv_() {
	    hot2.getPlugin("exportFile").downloadFile("csv", {
        filename: "table export",
        columnDelimiter: ';',
        columnHeaders: true

    });
};