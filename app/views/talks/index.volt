<div ng-controller="TalksIndexCtrl" style="text-align:right;">

<div><input type="text" ng-model="delayTime" style="width:50px"/> (s)</div>
<div>Volume <input type="text" ng-model="volume" style="width:50px"/></div>
<div><input type="checkbox" ng-model="isStop" /></div>
<div>
<select id="lesson" ng-model="currentLesson">
	<option ng-repeat="lesson in lessons" value="[[ lesson.id ]]">[[ lesson.name ]]</option>	
</select>
</div>

<audio ng-repeat="item in itemList" id="audio-[[ item.id ]]" src="[['/media/talk/' + item.file_path]]"></audio>
</div>

<script src="/ng-app/controllers/talks_index.js"></script>