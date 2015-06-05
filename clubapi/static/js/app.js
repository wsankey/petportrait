var ppcApp;
var ppcApp = angular.module('ppcApp', []);
ppcApp.controller('formController', function($scope) {
	$scope.master = {firstName: "John",
					 lastName: "Doe"};
	$scope.reset = function() {
		$scope.user = angular.copy($scope.master);
	};
	$scope.reset();
});

