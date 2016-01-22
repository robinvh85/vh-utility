<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        {{ get_title() }}
        <link rel="stylesheet" href="/css/bootstrap.min.css">
        <link rel="stylesheet" href="/css/main.css">
        <script src="/js/jquery-2.1.4.min.js"></script>
        <script src="/js/bootstrap.min.js"></script>
        <script src="/plugins/angular/js/angular.min.js"></script>
		<script>
			angular.module("app", ["ngResource", "ui.bootstrap"]).config(function($interpolateProvider) {
				$interpolateProvider.startSymbol('[[');
				$interpolateProvider.endSymbol(']]');
			});	
			
			Array.prototype.sortBy = function(p, type) {
				if(type == undefined) type = "asc";

				if(type == "desc"){
					return this.slice(0).sort(function(a,b) {
						return (a[p] < b[p]) ? 1 : (a[p] > b[p]) ? -1 : 0;
					});				
				} else {
					return this.slice(0).sort(function(a,b) {
						return (a[p] > b[p]) ? 1 : (a[p] < b[p]) ? -1 : 0;
					});	
				}	
			}
		</script>
    </head>
    <body style="padding:0px 20px;" ng-app="app">
            {{ content() }}
    </body>
	
	<script src="/plugins/angular/js/angular-resource.min.js"></script>
	<script src="/ng-app/factory/resources.js"></script>
	<script src="/plugins/angular/js/ui-bootstrap-tpls-0.14.3.min.js"></script>
</html>
