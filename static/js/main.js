$(document).ready(function() {
	console.log("Ready!!!");


	$('#sidebar').each(function(){
		$(this).find('.sel').each(function() {
			$(this).click(function(){
				var nombre = 'Grafico' + $(this).text();
				$("#name").text(nombre)
			
				//Manda el cambio de "variable"
			    $.ajax({
			        url: "/",
			        type: "POST",
			        contentType: 'application/json;charset=UTF-8',
			        data: {
			            'dato': $(this).text()
			        },
			        dataType:"json",
			        success: function (data) {
			            Plotly.newPlot('bargraph', data );
			        }
			    });


			})
		});
	});
});