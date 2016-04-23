angular.module("app").controller("StatsRcbCtrl", function($scope, $timeout, $interval, resources) {

	$scope.site_id = 0;
	$scope.itemList = [];	
	
	function refreshData(){
		console.log("refreshData()");
		
		resources.stats.listRcb({site_id:$scope.site_id}).$promise.then(function(res) {
			$scope.itemList = res.data;	
		});			
	}	
	
	$scope.init = function(){
		refreshData();
	}
	
	//$scope.init();
});