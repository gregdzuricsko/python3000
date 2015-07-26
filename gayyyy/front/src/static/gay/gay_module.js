'use strict';

import { GayCtrl } from './gay_control'
import { GaySvc } from './gay_svc'

let ctrl = GayCtrl;
let svc = GaySvc.factory;

export { svc };
export { ctrl };
