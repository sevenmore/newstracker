angular.module('newstrackerService', ['ngResource'])
    .factory('Inrss', function($resource){
        return $resource('/api/v1/rssin', {}, {
            query: {method:'GET', isArray:false}
        });
    });
