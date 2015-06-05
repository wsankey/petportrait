// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('ppc.services', ['ngResource'])
  .factory('Owner', function($resource) {
    return $resource('/api/owner/:id/'); 
  })
  .factory('User', function($resource) {
    return $resource('/api/pet/:id/'); 
  });