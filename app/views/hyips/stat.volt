
<div ng-controller="HyipStatCtrl" ng-init="init({{ site_id }})">
	<h4>{{ site_url }}</h4>
	<input type="text" ng-model="fromDate" style="width:80px;"/> - <input type="text" ng-model="toDate" style="width:80px;"/> 
	<button class="btn btn-primary btn-sm" ng-click="refreshData()">Add</button>
	<div id="chart_increase"></div>
	<div id="chart_invest"></div>
	<div id="chart_acc"></div>
</div>

<script src="/ng-app/controllers/hyip_stat.js"></script>