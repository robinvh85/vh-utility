<div ng-controller="WordIndexCtrl" style="text-align:right;">

<div><input type="text" ng-model="delayTime" style="width:50px"/> (s)</div>
<div><input type="checkbox" ng-model="isStop" /></div>
<div>
<select id="category" ng-model="category">
	<option value="Nihongo_1">Nihongo_1</option>
	<option value="Nihongo_2">Nihongo_2</option>
	<option value="Nihongo_3">Nihongo_3</option>
	<option value="Nihongo_4">Nihongo_4</option>
	<option value="Nihongo_5">Nihongo_5</option>
</select>
</div>

<audio ng-repeat="item in itemList" id="audio-[[ item.id ]]" src="[['/media/audio/' + item.audioPath]]"></audio>
</div>

<script src="/ng-app/controllers/word_index.js"></script>