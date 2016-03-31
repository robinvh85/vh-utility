<style>
.input-sm{
	height:25px;
}

.table-hover tbody tr:hover td, .table-hover tbody tr:hover th {
  background-color: #fbf6dd;
}
</style>

<div ng-controller="HyipIndexCtrl">

<table class="table table-bordered table-hover table-striped">
	<thead>
		<tr>
			<td style="width:30px;"></td>
			<td style="width:250px;">URL</td>
			<td style="width:120px;">Note <input type="checkbox" ng-model="isSortByNote" /></td>
			<td style="width:80px;">Type</td>
			<td style="width:110px;">Start At</td>
			<td style="width:40px;">Life</td>
			<td style="width:40px;">Scam</td>
			<td style="width:200px;">Monitor</td>
			<td style="width:40px;">Stat</td>
			<td></td>
		</tr>		
	</thead>
	<tbody>
	<tr ng-repeat="item in itemList | orderBy:sortBy" >
		<td>[[ $index + 1 ]]</td>
		<td><a href="http://[[ item.url ]]" target="_blank">[[ item.url ]]</a>
		- <a href="/hyips/stat?site_id=[[ item.site_id ]]" ng-show="item.is_stat == 1" target="_blank">Stat</a>
		- <a href="https://www.google.com/#q=[[ item.url ]]" target="_blank">Google</a>
		</td>
		<td><input type="text" ng-model="item.note" style="width:110px" class="form-control input-sm" ng-blur="updateMonitorSite(item)" /></td>
		<td>
			<select ng-model="item.type" ng-change="updateSite(item)">
				<option ng-repeat="item in typeList" value="[[ item ]]">[[ item ]]</option>
			</select>
		</td>
		<td><input type="text" ng-model="item.start_at" style="width:85px" class="form-control input-sm" ng-blur="updateSite(item)" /></td>
		<td style="text-align:center;"> [[ calLifeTime(item.start_at) ]] </td>	
		<td style="text-align:center;"><input type="checkbox" ng-model="item.is_scam" ng-true-value="'1'" ng-false-value="'0'" ng-change="updateSite(item)"/></td>
		<td><a href="[[ item.ref_site_url ]]" target="_blank">[[ item.monitor ]]</a></td>		
		<td><input type="checkbox" ng-model="item.is_stat" ng-true-value="'1'" ng-false-value="'0'" ng-change="updateSite(item)"/></td>
		<td></td>
	</tr>
	</tbody>
	<tfoot>
	<tr>
			<td></td>
			<td><input type="text" ng-model="newItem.url" class="form-control input-sm" /></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td>
				<input type="text" ng-model="newItem.monitor" class="form-control input-sm" placeholder="Monitor" style="width:100px; display:inherit;"/>
				<input type="text" ng-model="newItem.ref_site_id" class="form-control input-sm" placeholder="ID" style="width:70px; display:inherit;"/>
			</td>
			<td></td>
			<td><button class="btn btn-primary btn-sm" ng-click="addNewItem()">Add</button></td>
		</tr>
	</tfoot>
</table>
<hr>
<table class="table table-bordered table-hover table-striped">
	<thead>
		<tr>
			<td style="width:30px;"></td>
			<td style="width:250px;">RCB URL</td>
			<td style="width:150px;">Monitor</td>
			<td style="width:80px;">Done</td>
			<td></td>
		</tr>		
	</thead>
	<tr ng-repeat="item in itemUnknowList" >
		<td>[[ $index + 1 ]]</td>
		<td><a href="[[ item.url ]]" target="_blank">[[ item.url ]]</a></td>
		<td>[[ item.monitor ]]</td>
		<td style="text-align:center;"><input type="checkbox" ng-model="item.is_done" ng-true-value="'1'" ng-false-value="'0'" ng-change="updateUnknowSite(item)"/></td>
		<td></td>
	</tr>
</table>

<script src="/ng-app/controllers/hyip_index.js"></script>