<div ng-controller="WordCtrl">

	<div class="">
		<nav>
			<ul class="pager">
				<li class="previous"><a href="#" ng-click="refreshTable()">Refresh</a></li>
				<li class="next"><a href="#" ng-click="showCreate()">Create</a></li>
			</ul>
		</nav>
	</div> 	

	<table class="table table-bordered table-hover table-striped"> 
		<thead> 
			<tr> 
				<th style="width:50px;">ID</th> 
				<th>Text</th> 
				<th></th>
			</tr> 
		</thead> 
		<tbody> 
		<tr ng-repeat="item in dataList"> 
			<td>[[ item.id ]]</td>
			<td>[[ item.text ]]</td>
			<td><a href="#" ng-click="showEdit(item)">Edit</a></td>
		</tr> 
		</tbody> 
	</table>
	
	<uib-pagination total-items="fullDataList.length" ng-model="currentPage" items-per-page="itemPerPage"></uib-pagination>

	<!-- Modal -->
	<div class="modal fade" id="frmModal" tabindex="-1" role="dialog">
	  <div class="modal-dialog" role="document">
		<div class="modal-content">
		  <div class="modal-header">
			<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
			<h4 class="modal-title" id="myModalLabel">[[ action ]]</h4>
		  </div>
		  <div class="modal-body">
			<form class="form-horizontal">
			  <div class="form-group">
				<label for="text" class="col-sm-2 control-label">Text</label>
				<div class="col-sm-10">
					<input type="text" class="form-control" id="text" ng-model="currentObj.text">
				</div>
			  </div>
			  <div class="form-group">
				<label for="meaning" class="col-sm-2 control-label">Meaning</label>
				<div class="col-sm-10">
					<input type="text" class="form-control" id="meaning" ng-model="currentObj.meaning">
				</div>
			  </div>
			</form>
		  </div>
		  <div class="modal-footer">
			<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
			<button type="button" class="btn btn-primary" ng-click="save()">Save changes</button>
		  </div>
		</div>
	  </div>
	</div>

</div>

<script src="/ng-app/controllers/word.js"></script>