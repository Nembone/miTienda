var app = angular.module('app', []);

app.controller('DolarCtrl', function($scope, $http) {
    $scope.dailyIndicators = '';
    $http.get('https://mindicador.cl/api/dolar').then(function(res) {  //.success se cambio por .then // 
        $scope.dailyIndicators = res.data.serie[0].valor;  // se toma el ultimo valor del dolar // 
    })
});

