setActivePage('nav_home');
document.getElementById('stats-generator').click();


if (document.querySelector('.jscolor').value == '000000' ){
	document.getElementById('off-button').classList.add('disabled');
	document.getElementById('set-default-button').classList.add('disabled');
} else {
	document.getElementById('off-button').classList.remove('disabled');
	document.getElementById('set-default-button').classList.remove('disabled');
}

function submit(setDefault=false, useDefault=false,turnOff=false){
	if (setDefault) {
		document.getElementById('set-as-default').checked = true;
	}
	if (useDefault) {
		document.getElementById('change-to-default').checked = true;
	}
	if (turnOff) {
		document.getElementById('turn-off').checked = true;
	}

	document.getElementById('color-form').submit();
}


function analyse(temperatureData, humidityData, onData){
    var temperatureRenderData = {
        datasets: [{
            data: temperatureData,
            backgroundColor: ['#123456', '#99ff11', '#128345']
        }],
        label: ['Hot', 'Comfortable', 'Cold']
        
    };
    var humidityRenderData = {
        datasets: [{
            data: humidityData,
            backgroundColor: ['#123456', '#99ff11', '#128345']
        }],
        label: ['Humid', 'Comfortable', 'Dry']
        
    };
    var onRenderData = {
        datasets: [{
            data: onData,
            backgroundColor: ['#123456', '#99ff11']
        }],
        label: ['On', 'Off']
        
    };
    
	renderChart(document.getElementById('temperature-chart'), temperatureRenderData);
	renderChart(document.getElementById('humidity-chart'), humidityRenderData);
	renderChart(document.getElementById('on-chart'), onRenderData);
}

function renderChart(ctx, data) {
    
	
	var onCtx = document.getElementById('on-chart');
	var myDoughnutChart = new Chart(ctx, {	  
		type: 'doughnut',
   		data: data,
		options: {
			legend: {
				display: false,
			}
		}
	});
}
