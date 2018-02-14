google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChartRAM);
google.charts.setOnLoadCallback(drawChartDISQUE);
google.charts.setOnLoadCallback(drawChartCPU);

function drawChartRAM() {
  var use = parseInt(document.getElementById('occupation_ram').textContent);
  var data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'],
    ['RAM utilisée',     use ],
    ['RAM libre',         100 - use]
  ]);
  var options = {
    'title': 'Occupation de la RAM',
    'is3D': true,
    'width':350,
    'height':300,
    'colors':['#4AB9AA','#A9C0FE'],
    'tooltip.text':'value',

  };
  var chart = new google.visualization.PieChart(document.getElementById('ram_usage'));
  chart.draw(data, options);
}

function drawChartDISQUE() {
  var use = parseInt(document.getElementById('occupation_disque').textContent);
  var data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'],
    ['Mémoire utilisée',     use ],
    ['Mémoire libre',         100 - use]
  ]);
  var options = {
    'title': 'Occupation du stockage',
    'is3D': true,
    'width':350,
    'height':300,
    'colors':['#E6E152','#F6A731'],
    'tooltip.text':'value',
  };
  var chart = new google.visualization.PieChart(document.getElementById('disque_usage'));
  chart.draw(data, options);
}

function drawChartCPU() {
  var use = parseInt(document.getElementById('utilisation_cpu').textContent);
  var data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'],
    ['CPU utilisée',     use ],
    ['CPU libre',         100 - use]
  ]);
  var options = {
    'title': 'Occupation des CPU',
    'is3D': true,
    'width':350,
    'height':300,
    'colors':['#F6315F','#5831F6'],
    'tooltip.text':'value',
  };
  var chart = new google.visualization.PieChart(document.getElementById('cpu_usage'));
  chart.draw(data, options);
}
