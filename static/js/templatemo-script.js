/*
 *	www.templatemo.com
 *******************************************************/

/* HTML document is loaded. DOM is ready. 
-----------------------------------------*/
$(document).ready(function(){

	/* Mobile menu */
	$('.mobile-menu-icon').click(function(){
		$('.templatemo-left-nav').slideToggle();				
	});

	/* Close the widget when clicked on close button */
	$('.templatemo-content-widget .fa-times').click(function(){
		$(this).parent().slideUp(function(){
			$(this).hide();
		});
	});
});

// google.load('visualization', '1.0', {'packages':['corechart']});

//       // Set a callback to run when the Google Visualization API is loaded.
//       google.setOnLoadCallback(drawChart); 
      
//       // Callback that creates and populates a data table,
//       // instantiates the pie chart, passes in the data and
//       // draws it.
//       function drawChart() {

//           // Create the data table.
//           var data = new google.visualization.DataTable();
//           data.addColumn('string', 'Topping');
//           data.addColumn('number', 'Slices');
//           data.addRows([
//             ['Mushrooms', 3],
//             ['Onions', 1],
//             ['Olives', 1],
//             ['Zucchini', 1],
//             ['Pepperoni', 2]
//           ]);

//           // Set chart options
//           var options = {'title':'How Much Pizza I Ate Last Night'};

//           // Instantiate and draw our chart, passing in some options.
//           var pieChart = new google.visualization.PieChart(document.getElementById('pie_chart_div'));
//           pieChart.draw(data, options);

//           var barChart = new google.visualization.BarChart(document.getElementById('bar_chart_div'));
//           barChart.draw(data, options);
//       }

//       jQuery(document).ready(function(){
//         if(jQuery.browser.mozilla) {
//           //refresh page on browser resize
//           // http://www.sitepoint.com/jquery-refresh-page-browser-resize/
//           jQuery(window).bind('resize', function(e)
//           {
//             if (window.RT) clearTimeout(window.RT);
//             window.RT = setTimeout(function()
//             {
//               this.location.reload(false); /* false to get page from cache */
//             }, 200);
//           });      
//         } else {
//           jQuery(window).resize(function(){
//             drawChart();
//           });  
//         }   
//       });