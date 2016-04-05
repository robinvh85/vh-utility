<style>
.ng-datepicker-input{
	width:90px;
}
</style>

<div ng-controller="HyipStatCtrl" ng-init="init({{ site_id }})">
	<h4>{{ site_url }}</h4>
	<ng-datepicker ng-model="fromDate" format="YYYY/MM/DD" view-format="YYYY/MM/DD" style="float:left;"></ng-datepicker>
	<ng-datepicker ng-model="toDate" format="YYYY/MM/DD" view-format="YYYY/MM/DD" style="margin-left:10px; float:left;"></ng-datepicker> 
	<button class="btn btn-primary btn-sm" ng-click="refreshData()" style="margin-left:10px; float:left;">Submit</button>
	<div style="clear:both;"></div>
	<div id="chart_increase"></div>
	<div id="chart_invest"></div>
	<div id="chart_acc"></div>
</div>

<script src="/ng-app/controllers/hyip_stat.js"></script>