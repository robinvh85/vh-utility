<style>
.input-sm{
	height:25px;
}

.table-hover tbody tr:hover td, .table-hover tbody tr:hover th {
  background-color: #fbf6dd;
}

.red{
	color:red;
}
</style>

<div ng-controller="HyipInvestCtrl" ng-init="init({{ site_id }})">

<table class="table table-bordered table-hover table-striped">
	<thead>
		<tr>
			<td style="width:30px;"></td>
			<td style="width:250px;">Site</td>
			<td style="width:150px;">Monitor</td>
			<td style="width:110px;">Acc</td>
			<td style="width:40px;">Amount</td>			
			<td style="width:100px;">Time</td>
			<td style="width:100px;">IP</td>
			<td></td>
		</tr>
		<tr ng-show="siteId">
			<td></td>
			<td></td>
			<td><input type="text" ng-model="newItem.monitor" style="width:150px;"/></td>
			<td><input type="text" ng-model="newItem.acc_name" style="width:100px;"/></td>
			<td><input type="text" ng-model="newItem.amount" style="width:70px;"/></td>
			<td><input type="text" ng-model="newItem.time" style="width:150px;"/></td>
			<td><input type="text" ng-model="newItem.ip" style="width:150px;"/></td>
			<td><button class="btn btn-primary btn-sm" ng-click="addNewItem()">Add</button></td>
		</tr>
	</thead>
	<tbody>
	<tr ng-repeat="item in itemList" ng-class="newItem.ip == item.ip?'red':''">
		<td>[[ $index + 1 ]]</td>
		<td><a href="http://[[ item.url ]]" target="_blank">[[ item.url ]]</a>
		- <a href="/hyips/stat?site_id=[[ item.site_id ]]" ng-show="item.is_stat == 1" target="_blank">Stat</a>
		- <a href="https://www.google.com/#q=[[ item.url ]]" target="_blank">Google</a>
		</td>
		<td><a href="[[ item.ref_site_url ]]" target="_blank">[[ item.monitor ]]</a> <a href="#" style="margin-left:10px;" ng-click="newItem.monitor=item.monitor;"><span class="glyphicon glyphicon-plus"></span></a></td>		
		<td>[[ item.acc_name ]]</td>
		<td style="text-align:center;">[[ item.amount ]]</td>	
		<td>[[ item.time ]]</td>
		<td>[[ item.ip ]]</td>
		<td>
		<select ng-model='item.status' ng-change="updateInvest(item)">
			<option ng-repeat="status in statusList" ng-value="status">[[ status ]]</option>
		</select>
		</td>
		<td></td>
	</tr>
	</tbody>	
</table>
<hr>

<script src="/ng-app/controllers/hyip_invest.js"></script>