'use strict';
//example es6 class from engineering.iconnect360.com/angularjs/
//works for now until i usees6 to do file stuff
class UserSvc {
    constructor($http){
        this.$http = $http;
    }

    getUsers(){
        return this.$http.get('https://api.github.com/users').then(r => r.data);
    }

    static factory($http){
        return new UserSvc($http);
    }
};

//man, it's been a while since i've written javascripty stuff
UserSvc.factory.$inject = ['$http'];

export {UserSvc}
