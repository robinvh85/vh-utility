angular.module("app").controller("TalksIndexCtrl", function($scope, $timeout, $interval, resources) {

	$scope.itemList = [];
	$scope.isStop = false;
	$scope.delayTime = 5;
	$scope.currentLesson;
	$scope.lessons;
	$scope.timer = null;
	$scope.currentIndex = 0;
	$scope.volume = 0.5;
	
	function getRandomItem(){
		item = $scope.itemList[Math.floor(Math.random() * $scope.itemList.length)];
		return item;
	}
	
	function getNextItem(){
		item = $scope.itemList[$scope.currentIndex];
		$scope.currentIndex++;
		
		if($scope.currentIndex >= $scope.itemList.length){
			$scope.currentIndex = 0;
		}
		
		return item;
	}
	
	function playRandom(){
		if(!$scope.isStop){
			// var item = getRandomItem();
			var item = getNextItem();
			var audio = $("#audio-" + item.id);
			audio.prop("volume", $scope.volume);
			audio.trigger('play');
		}
		
		if(Number($scope.delayTime) < 3){
			$scope.delayTime = 3;			
		}
		
		$scope.timer = $timeout(playRandom, $scope.delayTime * 1000);
	}
	
	function refreshData(){
		var params = {
			lesson_id : $scope.currentLesson
		};
		
		resources.talks.list(params).$promise.then(function(res) {
			$scope.itemList = res.data;	
			playRandom();
		});	
	}
	
	function initData(){				
		if($scope.timer != null){
			$timeout.cancel($scope.timer);
		}
		
		resources.talks.listLesson().$promise.then(function(res) {
			$scope.lessons = res.data;			
			$scope.currentLesson = $scope.lessons[0].id;
			refreshData();
		});					
	}
	
	$scope.$watch('currentLesson', function(newValue, oldValue) {					
		if(oldValue && newValue != oldValue){
			$timeout.cancel($scope.timer);
			refreshData();
		}
	});
	
	$scope.init = function(){
		initData();
	}
	
	$scope.init();
});