angular.module("app").controller("HyipInvestCtrl", function($scope, $window, $timeout, $interval, resources) {

	$scope.itemList = [];	
	$scope.newItem = {};
	$scope.siteId = -1;
	$scope.statusList = ["Invest", "Pending", "OK", "NG"];
	
	$scope.addNewItem = function(){
		$scope.newItem.site_id = $scope.siteId;
		
		if(!$scope.newItem.monitor || !$scope.newItem.acc_name || !$scope.newItem.amount)
			return;
		
		resources.hyips2.createInvest($scope.newItem).$promise.then(function(res) {	
			if(res.status == "OK"){
				$scope.newItem = {};
				refreshData($scope.siteId);
			}
		});	
	}
	
	$scope.updateInvest = function(item){
		resources.hyips2.updateInvest(item).$promise.then(function(res) {	
			if(res.status == "OK"){
				console.log("Update success");
			}
		});	
	}
	
	function refreshData(site_id){
		console.log("refreshData()");
		var params = {	
			site_id : site_id
		};		
		
		resources.hyips2.listSiteInvest(params).$promise.then(function(res) {
			$scope.itemList = res.data;	
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
	
	$scope.init = function(site_id){
		$scope.siteId = site_id;
		
		refreshData(site_id);
		$scope.newItem.time = moment().format("YYYY/MM/DD hh:mm:ss");
		$scope.newItem.ip = $window.myip;
	}
});