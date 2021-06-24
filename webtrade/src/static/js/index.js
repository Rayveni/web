function main() {
    let table_data = get_data_to_js('/query_data?view_id=open_broker_report&params=_173364_');
    return set_total_account_html(table_data);
}

function set_total_account_html(_data) {
    let period = _data["title_info"]["period"];
    let acc_total = _data["account_totally"];

    let _header=document.getElementById("holdings_header");
	//_header.textContent=_header.textContent.replace("start",period[0]).replace("end",period[1]);


    let cb_value = currency_print(acc_total["assets_cb_value_fact"]["RUB"]["value"], "RUB", locale = 'ru'),
		cb_tooltip = acc_total["assets_cb_value_fact"]["text_description"];

    let card_holdings_overview = document.getElementById('acc_total'),
    tbl = document.createElement("table");
    tbl.id = "acc_total_table_id";

    let dt = [
	    ['','agr 173364','agr 173364','total'],
		['start date',period[0],period[0]],
		['end date',period[1],period[1]],
        ["Market Value", cb_value,cb_value,cb_value]

    ]
    generate_table_from_array(tbl, dt);
    card_holdings_overview.appendChild(tbl);
    return period;

}
var a = main();