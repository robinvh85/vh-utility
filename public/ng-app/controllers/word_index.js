angular.module("app").controller("WordIndexCtrl", function($scope, $timeout, $interval, resources) {

	$scope.itemList = [];
	$scope.isStop = false;
	$scope.delayTime = 5;
	$scope.category = "Nihongo_1";
	$scope.timer = null;
	
	function getRandomItem(){
		item = $scope.itemList[Math.floor(Math.random() * $scope.itemList.length)];
		return item;
	}
	
	function playRandom(){
		if(!$scope.isStop){
			var item = getRandomItem();
			console.log(item);
			$("#audio-" + item.id).trigger('play');
		}
		
		if(Number($scope.delayTime) < 3){
			$scope.delayTime = 3;			
		}
		
		$scope.timer = $timeout(playRandom, $scope.delayTime * 1000);
	}
	
	function refreshData(){
		var params = {
			category : $scope.category
		};
		
		if($scope.timer != null){
			$timeout.cancel($scope.timer);
		}
		
		resources.words.list(params).$promise.then(function(res) {
			$scope.itemList = res.data;	
			playRandom();
		});	
	}
	
	$scope.$watch('category', function(newValue, oldValue) {
		if(newValue != oldValue){
			refreshData();
		}
	});
	
	$scope.init = function(){
		refreshData();		
	}
	
	$scope.init();
});