angular.module("app").controller("WordCtrl", function($scope, resources) {
	$scope.currentObj = {};
	$scope.fullDataList = [];
	$scope.dataList = [];
	$scope.itemPerPage = 20;
	$scope.currentPage = 0;	
	
	$scope.action = "";
	
	/* Paging */
	$scope.$watch('currentPage + itemPerPage', function() {
		var begin = (($scope.currentPage - 1) * $scope.itemPerPage)
		var end = begin + $scope.itemPerPage;

		$scope.dataList = $scope.fullDataList.slice(begin, end);
	});
	
	$scope.showEdit = function(item){
		$scope.action = "Edit";
		$scope.currentObj = item;
		$('#frmModal').modal('toggle');
	}
	/* End Paging */
	
	$scope.showCreate = function(){
		$scope.action = "New";
		$scope.currentObj = {};

		$('#frmModal').modal('toggle');
	}

	$scope.changeActive = function(item){
		if(item.is_actived == "0" )
			item.is_actived = "1";
		else
			item.is_actived = "0";
		
		resources.words.save(item).$promise.then(function(res) {
			//console.log(res);
		});
	}

	$scope.save = function(){
		if($scope.action == "New"){
			resources.words.create($scope.currentObj).$promise.then(function(res) {
				$('#frmModal').modal('toggle');
				$scope.refreshTable();
			});
		}
		else {
			resources.words.save($scope.currentObj).$promise.then(function(res) {
				$('#frmModal').modal('toggle');
				$scope.refreshTable();
			});
		}
	}

	$scope.refreshTable = function(){
		resources.words.get().$promise.then(function(res) {
			$scope.fullDataList = res.data;			
			$scope.currentPage = 1;
		});
	}

	$scope.init = function(){
		$scope.refreshTable();				
	}

	$scope.init();
});