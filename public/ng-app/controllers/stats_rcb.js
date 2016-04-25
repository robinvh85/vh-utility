angular.module("app").controller("StatsRcbCtrl", function($scope, $timeout, $interval, resources) {

	$scope.site_id = 0;
	$scope.itemList = [];	
	$scope.itemTotalList = [];	
	
	function refreshData(){
		console.log("refreshData()");
		
		resources.stats.listRcb({site_id:$scope.site_id}).$promise.then(function(res) {
			$scope.itemList = res.data;	
		});

		resources.stats.listRcbTotal({site_id:$scope.site_id}).$promise.then(function(res) {
			$scope.itemTotalList = res.data;	
		});		
	}	
	
	$scope.init = function(){
		refreshData();
	}
	
	//$scope.init();
});