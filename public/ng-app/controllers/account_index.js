angular.module("app").controller("AccountIndexCtrl", function($scope, $window, resources) {

	$scope.itemList = [];	
	$scope.newItem = {};
	$scope.groups = ["VN","JP","SI","LD"];
	
	$scope.addNewItem = function(){
		if(!$scope.newItem.name)
			return;
		
		resources.accounts.create($scope.newItem).$promise.then(function(res) {	
			if(res.status == "OK"){
				$scope.newItem = {};
				refreshData();
			}
		});	
	}
	
	$scope.update = function(item){
		resources.accounts.update(item).$promise.then(function(res) {	
			if(res.status == "OK"){
				console.log("Update success");
			}
		});	
	}
	
	function refreshData(){
		console.log("refreshData()");
		
		resources.accounts.list().$promise.then(function(res) {
			$scope.itemList = res.data;	
		});			
	}	
	
	$scope.init = function(site_id){
		$scope.newItem.group = $scope.groups[0];
		
		refreshData();
	}
	
	$scope.init();
});