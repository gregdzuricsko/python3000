
class GayCtrl {

    constructor(gaySvc) {
        this.gaySvc = gaySvc;
        this.init();
    }

    init(){
      this.events = {};
      this.gaySvc.getEagleHappyHour().then(x => {
          this.events.eagleHappyHour = x.data;
      });
      this.gaySvc.getEagleSpecialEvents().then(x => {
          this.events.eagleSpecials = x.data;
      });
      this.gaySvc.getSaloonHappyHour().then(x => {
          this.events.saloonHappyHour = x.data;
      });
      this.gaySvc.getTownHouseSpecialEvents().then(x => {
          this.events.townHouseSpecials = x.data;
      });
      this.gaySvc.getGroundZeroSpecialEvents().then(x => {
          this.events.groundZeroSpecials = x.data;
      });
    }
}

GayCtrl.$inject = ['gaySvc'];

export {GayCtrl};
