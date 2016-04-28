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
<table class="table table-bordered table-hover table-striped" style="width:500px; float:left">
	<thead>
		<tr>
			<td style="width:40px;">No.</td>
			<td style="width:150px;">Date</td>
			<td style="width:200px;">Monitor</td>
			<td style="width:70px;">Count</td>
			<td style="width:100px;">Deposit</td>	
		</tr>		
	</thead>
	<tbody>
	<tr ng-repeat="item in itemList">
		<td>[[ $index + 1 ]]</td>
		<td>[[ item.date ]]</td>
		<td><a href="[[ item.ref_site_url ]]" target="_blank">[[ item.monitor ]]</a></td>		
		<td>[[ item.count ]]</td>
		<td>[[ item.deposit ]]</td>
	</tr>
	</tbody>	
</table>

<table class="table table-bordered table-hover table-striped" style="width:400px; float:left">
	<thead>
		<tr>
			<td style="width:40px;">No.</td>
			<td style="width:150px;">Date</td>
			<td style="width:70px;">Count</td>
			<td style="width:100px;">Deposit</td>	
		</tr>		
	</thead>
	<tbody>
	<tr ng-repeat="item in itemTotalList">
		<td>[[ $index + 1 ]]</td>
		<td>[[ item.date ]]</td>
		<td>[[ item.count ]]</td>
		<td>[[ item.deposit ]]</td>
	</tr>
	</tbody>	
</table>

<script src="/ng-app/controllers/stats_rcb.js"></script>