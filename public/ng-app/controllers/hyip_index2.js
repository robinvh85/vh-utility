angular.module("app").controller("HyipIndex2Ctrl", function($scope, $timeout, $interval, resources) {

	$scope.itemList = [];
	$scope.itemUnknowList = [];
	$scope.typeList = ["Hr", "1d", "3d", "7d", "10d", "15d", "30d", ">30d"];
	$scope.newItem = {}
	$scope.isSortByNote = false;
	$scope.accOrder = {"investvh":0, "deposit":1, "dollar":2, "money":3, "OK":4};
	$scope.investedSiteHash = {};
	
	
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
			id: item.id,
			start_at: item.start_at,
			is_scam: item.is_scam,
			is_stat: item.is_stat,
			type: item.type,
			note: item.note
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
		
		resources.hyips2.list(params).$promise.then(function(res) {
			$scope.itemList = res.data;	
		});			
	}	
	
	function refreshUnknowSiteData(){				
		resources.hyips.listUnknow().$promise.then(function(res) {
			$scope.itemUnknowList = res.data;	
		});	
	}	
	
	function createInvestedSiteHash(){
		for(var i=0; i<$scope.activeInvests.length; i++){
			$scope.investedSiteHash[$scope.activeInvests[i].site_id] = 1;
		}
		
		console.log($scope.investedSiteHash);
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
	
	$scope.checkActive = function(item){
		if($scope.investedSiteHash[item.id] == 1){
			return true;
		}
		
		return false;
	}
	
	$scope.init = function(){
		refreshData();
		refreshUnknowSiteData();
		createInvestedSiteHash();
	}
	
	//$scope.init();
});