'use strict';

class GayCtrl {
    constructor(gaySvc) {
        this.gaySvc = gaySvc;
        this.init();
    }

    init(){
      this.events = this.gaySvc.getEvents();
    }
}

GayCtrl.$inject = ['gaySvc'];

export {GayCtrl};
