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

<div ng-controller="StatsRcbCtrl" ng-init="site_id={{ site_id }}; init();">
<h4>{{ site_url }}</h4>
<table class="table table-bordered table-hover table-striped">
	<thead>
		<tr>
			<td style="width:40px;">No.</td>
			<td style="width:150px;">Date</td>
			<td style="width:200px;">Monitor</td>
			<td style="width:70px;">Count</td>
			<td style="width:100px;">Deposit</td>	
			<td>Note</td>
		</tr>		
	</thead>
	<tbody>
	<tr ng-repeat="item in itemList" ng-class="checkActive(item)?'active':''">
		<td>[[ $index + 1 ]]</td>
		<td>[[ item.date ]]</td>
		<td>[[ item.monitor ]]</td>
		<td>[[ item.count ]]</td>
		<td>[[ item.deposit ]]</td>
	</tr>
	</tbody>	
</table>

<script src="/ng-app/controllers/stats_rcb.js"></script>