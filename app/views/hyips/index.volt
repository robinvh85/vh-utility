<style>
.input-sm{
	height:25px;
}
</style>

<div ng-controller="HyipIndexCtrl">

<table class="table table-bordered table-hover table-striped">
	<thead>
		<tr>
			<td style="width:30px;"></td>
			<td style="width:200px;">URL</td>
			<td style="width:80px;">Type</td>
			<td style="width:110px;">Start At</td>
			<td style="width:40px;">Life</td>
			<td style="width:40px;">Scam</td>
			<td style="width:150px;">Monitor</td>
			<td style="width:40px;">Paid</td>						
			<td style="width:40px;">Google</td>
			<td></td>
		</tr>
	</thead>
	<tr ng-repeat="item in itemList" >
		<td>[[ $index + 1 ]]</td>
		<td><a href="http://[[ item.url ]]" target="_blank">[[ item.url ]]</a></td>
		<td>
			<select ng-model="item.type" ng-change="updateSite(item)">
				<option ng-repeat="item in typeList" value="[[ item ]]">[[ item ]]</option>
			</select>
		</td>
		<td><input type="text" ng-model="item.start_at" style="width:85px" class="form-control input-sm" ng-blur="updateSite(item)" /></td>
		<td style="text-align:center;"> [[ calLifeTime(item.start_at) ]] </td>	
		<td style="text-align:center;"><input type="checkbox" ng-model="item.is_scam" ng-true-value="'1'" ng-false-value="'0'" ng-change="updateSite(item)"/></td>
		<td><a href="[[ item.ref_site_url ]]" target="_blank">[[ item.monitor ]]</a></td>
		<td style="text-align:center;"><input type="checkbox" ng-model="item.is_paid" ng-true-value="'1'" ng-false-value="'0'" disabled="disabled"/></td>
		<td><a href="https://www.google.com/#q=[[ item.url ]]" target="_blank">Link</a></td>
		<td></td>
	</tr>
</table>

<script src="/ng-app/controllers/hyip_index.js"></script>