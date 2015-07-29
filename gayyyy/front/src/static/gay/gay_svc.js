//example es6 class from engineering.iconnect360.com/angularjs/
//works for now until i usees6 to do file stuff
class GaySvc {
  constructor($http) {
    this.$http = $http;
  }

  getEvents() {
    // maybe try out es6 promise stuff
    var docs = {};
    this.getEagleHappyHour().then(x =>{
      docs.eagleHappyHour = x;
      console.log("docs.eagleHappyHour = " + docs.eagleHappyHour);
    });
    this.getEagleSpecialEvents().then(x =>{
      docs.eagleSpecials = x;
      console.log("docs.eagleSpecials = " + docs.eagleSpecials);
    });
    this.getSaloonHappyHour().then(x =>{
      docs.saloonHappyHour = x;
      console.log("docs.saloonHappyHour = " + docs.saloonHappyHour);
    });
    this.getTownHouseSpecialEvents().then(x =>{
      docs.townHouseSpecials = x;
      console.log("docs.townHouseSpecials = " + docs.townHouseSpecials);
    });
    console.log(docs);
    return docs;
  }

  getEagleHappyHour() {
    return this.$http.get('json/EagleHappyHour.txt').then(r => r.data);
  }

  getSaloonHappyHour() {
    return this.$http.get('json/SaloonHappyHour.txt').then(r => r.data);
  }

  getEagleSpecialEvents() {
    return this.$http.get('json/EagleSpecials.txt').then(r => r.data);
  }

  getTownHouseSpecialEvents() {
      return this.$http.get('json/TownHouseSpecials.txt').then(r => r.data);
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
