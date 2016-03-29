angular.module("app").controller("HyipStatCtrl", function($scope, $timeout, $interval, resources) {
	
	function createChart(data){
		$('#chart').highcharts({
			chart: {
                zoomType: 'x'
            },
            title: {
                text: 'over time'
            },
            subtitle: {
                text: document.ontouchstart === undefined ?
                        'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                title: {
                    text: 'Exchange rate'
                }
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: {
                            x1: 0,
                            y1: 0,
                            x2: 0,
                            y2: 1
                        },
                        stops: [
                            [0, Highcharts.getOptions().colors[0]],
                            [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                        ]
                    },
                    marker: {
                        radius: 2
                    },
                    lineWidth: 1,
                    states: {
                        hover: {
                            lineWidth: 1
                        }
                    },
                    threshold: null
                }
            },

            series: [{
                type: 'area',
                name: 'Test',
				data: data
			}]
		});
	}
	
	$scope.init = function(){
		var params = {site_id:1};
		resources.hyips.listSiteStats(params).$promise.then(function(res) {
			//console.log("Updated Site", res);
			var list = res.data;
			var data = [];
			for(var i=0; i<list.length; i++){
				data[i] = []
				data[i].push(Number(list[i].time));
				data[i].push(Number(list[i].total_deposit));
			}
			
			console.log(data);
			//data = [];
			//data.push([1459268667000, 100]);
			//data.push([1459268756000, 110]);
			
			createChart(data);
		});
	}
	
	$scope.init();
});