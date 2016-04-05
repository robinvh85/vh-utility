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

<div ng-controller="AccountIndexCtrl">

<table class="table table-bordered table-hover table-striped">
	<thead>
		<tr>
			<td style="width:30px;"></td>
			<td style="width:80px;">Group</td>
			<td style="width:100px;">Name</td>
			<td style="width:90px;">PM</td>
			<td style="width:50px;">Amount</td>
			<td style="width:180px;">Email</td>
			<td style="width:200px;">Note</td>
			<td></td>
		</tr>
		<tr>
			<td></td>
			<td>
			<select ng-model="newItem.group" style="width:70px;">
				<option ng-repeat="item in groups" value="[[ item ]]">[[ item ]]</option>
			</select>
			</td>
			<td><input type="text" ng-model="newItem.name" style="width:100px;"/></td>
			<td><input type="text" ng-model="newItem.pm" style="width:90px;"/></td>
			<td><input type="text" ng-model="newItem.amount" style="width:50px;"/></td>
			<td><input type="text" ng-model="newItem.email" style="width:180px;"/></td>
			<td><input type="text" ng-model="newItem.note" style="width:200px;"/></td>
			<td><button class="btn btn-primary btn-sm" ng-click="addNewItem()">Add</button></td>
		</tr>			
	</thead>
	<tbody>
	<tr ng-repeat="item in itemList" ng-class="item.amount != '0' && item.amount != '' ? 'active' : ''">
		<td>[[ $index + 1 ]]</td>
		<td>[[ item.group ]]</td>
		<td>[[ item.name ]]</td>
		<td>[[ item.pm ]]</td>
		<td><input type="text" ng-model="item.amount" style="width:50px;" ng-blur="update(item)"/></td>		
		<td>[[ item.email ]]</td>
		<td><input type="text" ng-model="item.note" style="width:200px;" ng-blur="update(item)"/></td>
		<td></td>
	</tr>
	</tbody>	
</table>

<script src="/ng-app/controllers/account_index.js"></script>