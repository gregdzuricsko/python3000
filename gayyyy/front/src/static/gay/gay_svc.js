//example es6 class from engineering.iconnect360.com/angularjs/
//works for now until i usees6 to do file stuff
class GaySvc {
    constructor($http){
        this.$http = $http;
    }

    getHappyHourJson(){
        // maybe try out es6 promise stuff
        return this.$http.get('json/happyHour.txt').then(r => r.data);
    }

    static factory($http){
        return new GaySvc($http);
    }
}

//man, it's been a while since i've written javascripty stuff
GaySvc.factory.$inject = ['$http'];

export {GaySvc};
