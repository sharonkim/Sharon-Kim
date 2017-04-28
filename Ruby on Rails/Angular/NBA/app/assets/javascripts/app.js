var app = angular.module('nbaApp', ['ngRoute']);
app.config(function($routeProvider) {
    $routeProvider
        .when("/players",  {
            templateUrl: "/partials/players_partial.html",
            controller: "playersController",
        })
        .when("/teams", {
            templateUrl: "/partials/teams_partial.html",
            controller: "teamsController",
        })
        .otherwise({
            templateUrl: "/partials/players_partial.html",
            controller: "playersController",
        })
});

app.factory("playerFactory", function($http) {
    var factory = {};
    factory.index = function(callback) {
        $http.get("/players").success(function(output) {
            // console.log(playerFactory);
            callback(output);
        })
    }
    factory.create = function(newPlayer, callback) {
        $http.post("/players, newPlayer").success(fucntion(output));
            if (output.status){
                callback();
            }
        })
    }
    return factory;
})

app.controller("playersController", function($scope, playerFactory) {
    playerFactory.index(function(players) {
        $scope.players = players;
    });
    $scope.createPlayer = function(){
        playerFactory.create($scope.newPlayer, function(players) {
            $scope.players = players;
        });
    }
    console.log($scope.newPlayer);
})

app.factory("teamFactory", function($http) {
    var factory = {};
    factory.index = function(callback) {
        $http.get("/teams").success(function(output) {
            callback(output);
        })
    }
    return factory;
})

app.controller("teamsController", function($scope, teamFactory) {
    teamFactory.index(function(teams) {
        $scope.teams = teams;
    })
})
    // $scope.players = [
//         {firstName: "Michael", lastName: "Jordan"},
//         {firstName: "Kobe", lastName: "Bryant"},
//         {firstName: "Kevin", lastName: "Garnett"},
//         {firstName: "LeBron", lastName: "James"},
//         {firstName: "Stephen", lastName: "Curry"},
//         {firstName: "Jordan", lastName: "Clarkson"},
//         {firstName: "Derek", lastName: "Fisher"},
//         {firstName: "Jimmy", lastName: "Butler"},
//     ]
})

// app.controller("teamsController", function($scope) {
//     $scope.teams = [
        // {name: "Boston Celtics"},
        // {name: "Brooklyn Nets"},
        // {name: "New York Knicks"},
        // {name: "Philadelphia 76ers"},
        // {name: "Toronto Rapters"},
        // {name: "Chicago Bulls"},
        // {name: "Cleveland Cavaliers"},
        // {name: "Detroit Pistons"},
        // {name: "Indiana Pacers"},
        // {name: "Milwaukee Bucks"},
        // {name: "Atlanta Hawks"},
        // {name: "Charlotte Hornets"},
        // {name: "Miami Heat"},
        // {name: "Orlando Magic"},
        // {name: "Washington Wizards"},
        // {name: "Denver Nuggets"},
        // {name: "Minnesota Timberwolves"},
        // {name: "Oklahoma City Thunder"},
        // {name: "Portland Trail Blazers"},
        // {name: "Utah Jazz"},
        // {name: "Golden State Warriors"},
        // {name: "Los Angeles Clippers"},
        // {name: "Los Angeles Lakers"},
        // {name: "Phoenix Suns"},
        // {name: "Sacramento Kings"},
        // {name: "Dallas Mavericks"},
        // {name: "Houston Rockets"},
        // {name: "Memphis Grizzlies"},
        // {name: "New Orleans Pelicans"},
        // {name: "San Antonio Spurs"}
//     ]
})
