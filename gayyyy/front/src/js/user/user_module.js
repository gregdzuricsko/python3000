'use strict';

import { UserCtrl } from './user_control'
import { UserSvc } from './user_svc'

let ctrl = UserCtrl;
let svc = UserSvc.factory;

export { svc };
export { ctrl };
