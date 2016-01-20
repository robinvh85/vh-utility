<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <title>Template</title>
        <link rel="stylesheet" href="/css/bootstrap.min.css">
        <link rel="stylesheet" href="/css/main.css">
        <script src="/js/jquery-2.1.4.min.js"></script>
        <script src="/js/bootstrap.min.js"></script>
        <script src="/plugins/angular/js/angular.min.js"></script>
		<script>
			angular.module("app", ["ngResource"]).config(function($interpolateProvider) {
				$interpolateProvider.startSymbol('[[');
				$interpolateProvider.endSymbol(']]');
			});	
		</script>
    </head>
    <body style="padding:0px 20px;" ng-app="app">
            {{ content() }}
    </body>
	
	<script src="/plugins/angular/js/angular-resource.min.js"></script>
	<script src="/ng-app/factory/resources.js"></script>
</html>
