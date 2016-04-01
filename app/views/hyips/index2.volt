<style>
.input-sm{
	height:25px;
}

.table-hover tbody tr:hover td, .table-hover tbody tr:hover th {
  background-color: #fbf6dd;
}

.active td{
	background-color: #cceebb !important;
}
</style>

<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Sites</a>
    </div>
    <ul class="nav navbar-nav">
      <li><a href="/info/index" target="_blank">Info</a></li>
    </ul>
  </div>
</nav>

<div ng-controller="HyipIndex2Ctrl" ng-init='activeInvests={{ activeInvests }}; init();'>

<table class="table table-bordered table-hover table-striped">
	<thead>
		<tr>
			<td style="width:30px;"></td>
			<td style="width:250px;">URL</td>
			<td style="width:40px;">Stat</td>
			<td style="width:80px;">Type</td>
			<td style="width:110px;">Start At</td>
			<td style="width:40px;">Life</td>
			<td style="width:40px;">Scam</td>			
			<td></td>
			<td></td>
		</tr>		
	</thead>
	<tbody>
	<tr ng-repeat="item in itemList | orderBy:sortBy" ng-class="checkActive(item)?'active':''">
		<td>[[ $index + 1 ]]</td>
		<td><a href="http://[[ item.url ]]" target="_blank">[[ item.url ]]</a>
		- <a href="/hyips/stat?site_id=[[ item.id ]]" ng-show="item.is_stat == 1" target="_blank">Stat</a>
		- <a href="https://www.google.com/#q=[[ item.url ]]" target="_blank">Google</a>
		</td>
		<td><input type="checkbox" ng-model="item.is_stat" ng-true-value="'1'" ng-false-value="'0'" ng-change="updateSite(item)"/></td>
		<td>
			<select ng-model="item.type" ng-change="updateSite(item)">
				<option ng-repeat="item in typeList" value="[[ item ]]">[[ item ]]</option>
			</select>
		</td>
		<td><input type="text" ng-model="item.start_at" style="width:85px" class="form-control input-sm" ng-blur="updateSite(item)" /></td>
		<td style="text-align:center;"> [[ calLifeTime(item.start_at) ]] </td>	
		<td style="text-align:center;"><input type="checkbox" ng-model="item.is_scam" ng-true-value="'1'" ng-false-value="'0'" ng-change="updateSite(item)"/></td>		
		<td><a href="/hyips/invest?site_id=[[ item.id ]]" target="_blank">Invest</a></td>
		<td></td>
	</tr>
	</tbody>	
</table>
<hr>
<table class="table table-bordered table-hover table-striped">
	<thead>
		<tr>
			<td style="width:30px;"></td>
			<td style="width:250px;">RCB URL</td>
			<td style="width:230px;">Monitor</td>
			<td style="width:60px;">Done</td>
			<td></td>
		</tr>		
		<tr>
			<td></td>
			<td><input type="text" ng-model="newItem.url" class="form-control input-sm" /></td>
			<td>
				<input type="text" ng-model="newItem.monitor" class="form-control input-sm" placeholder="Monitor" style="width:120px; display:inherit;"/>
				<input type="text" ng-model="newItem.ref_site_id" class="form-control input-sm" placeholder="ID" style="width:80px; display:inherit;"/>
			</td>
			<td><button class="btn btn-primary btn-sm" ng-click="addNewItem()">Add</button></td>
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

<script src="/ng-app/controllers/hyip_index2.js"></script>