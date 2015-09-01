//example es6 class from engineering.iconnect360.com/angularjs/
//works for now until i usees6 to do file stuff
class GaySvc {
    constructor($http) {
        this.$http = $http;
    }

    getEagleHappyHour() {
        return this.$http.get('json/EagleHappyHour.txt');
    }

    getSaloonHappyHour() {
        return this.$http.get('json/SaloonHappyHour.txt');
    }

    getEagleSpecialEvents() {
        return this.$http.get('json/EagleSpecials.txt');
    }

    getTownHouseSpecialEvents() {
        return this.$http.get('json/TownHouseSpecials.txt');
    }

    getGroundZeroSpecialEvents() {
        return this.$http.get('json/GroundZeroSpecials.txt');
    }

    static factory($http) {
        return new GaySvc($http);
    }
}

//man, it's been a while since i've written javascripty stuff
GaySvc.factory.$inject = ['$http'];

export {
    GaySvc
};
