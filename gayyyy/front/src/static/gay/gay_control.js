'use strict';

class GayCtrl {
    constructor(gaySvc) {
        this.gaySvc = gaySvc;
        this.init();
    }

    init(){
        this.gaySvc.getHappyHourJson().then(happyHourEvents => {
            this.happyHourEvents = happyHourEvents;
            console.log(happyHourEvents);
        });
    }
}

GayCtrl.$inject = ['gaySvc'];

export {GayCtrl};
