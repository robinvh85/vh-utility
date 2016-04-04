angular.module("app").controller("HyipIndexCtrl", function($scope, $timeout, $interval, resources) {

	$scope.itemList = [];
	$scope.itemUnknowList = [];
	$scope.typeList = ["Hr", "1d", "3d", "7d", "10d", "15d", "30d", ">30d"];
	$scope.newItem = {}
	$scope.isSortByNote = false;
	$scope.accOrder = {"investvh":0, "deposit":1, "dollar":2, "money":3, "OK":4};
	
	$scope.startAtChange = function(index){
		console.log(index);
	}
	
	$scope.changeIsPaid = function(item){
		console.log(item);
	}
	
	$scope.updateMonitorSite = function(item){
		resources.hyips.updateMonitorSite(item).$promise.then(function(res) {
			console.log("Updated Site", res);
		});	
	}
	
	$scope.updateSite = function(item){
		var params = {
			id: item.site_id,
			start_at: item.start_at,
			is_scam: item.is_scam,
			is_stat: item.is_stat,
			type: item.type
		};
		
		resources.hyips.updateSite(params).$promise.then(function(res) {
			console.log("Updated Site", res);
		});	
	}

	$scope.updateUnknowSite = function(item){
		resources.hyips.updateUnknowSite(item).$promise.then(function(res) {
			console.log("Updated UnknowSite", res);
		});	
	}
	
	
	$scope.addNewItem = function(){
		resources.hyips.create($scope.newItem).$promise.then(function(res) {
			console.log("Updated Site", res);
			
			if(res.status == "OK"){
				$scope.newItem = {};
				refreshData();
			}
		});	
	}
	
	$scope.calLifeTime = function(dateString){
		if(!dateString) return "";
		
		var dt = moment(dateString);
		var now = moment();
		
		return now.diff(dt, 'days');
	}
	
	function refreshData(){
		console.log("refreshData()");
		var params = {			
		};		
		
		resources.hyips.list(params).$promise.then(function(res) {
			$scope.itemList = res.data;	
		});			
	}	
	
	function refreshUnknowSiteData(){				
		resources.hyips.listUnknow().$promise.then(function(res) {
			$scope.itemUnknowList = res.data;	
		});	
	}	
	
	$scope.sortBy = function(item){
		if($scope.isSortByNote){
			if(item.note != null){
				for(key in $scope.accOrder){
					if(item.note.indexOf(key) != -1){
						return $scope.accOrder[key];
					}
				}
			}
		}
	}
	
	$scope.init = function(){
		refreshData();
		refreshUnknowSiteData();
	}
	
	$scope.init();
});