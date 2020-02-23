function get_data_to_js(url) {

$.ajax({
                type: "POST",
                url: url,
                data: "dd",
				contentType:"application/json; charset=UTF-8",
			    
                type: 'POST',
				async: false,
                success: function(response) {
			
                     data1 = JSON.parse(response)  ;                
                },
                error: function(error) {
                    console.log(error);
                }
            });
return data1
}