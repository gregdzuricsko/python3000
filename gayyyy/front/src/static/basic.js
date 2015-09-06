"format es6";
import * as GayModule from './gay/gay_module';
import angular from 'angular';
console.log("help");

var app = angular.module('gay', [])
    .factory('gaySvc', GayModule.svc)
    .controller('gayCtrl', GayModule.ctrl);
