"format es6";
import * as UserModule from './user/user_module';
import * as GayModule from './gay/gay_module';
import angular from 'angular';

console.log(angular.version);
angular.module('gay',[])
.factory('gaySvc', GayModule.svc)
.controller('gayCtrl', GayModule.ctrl);
