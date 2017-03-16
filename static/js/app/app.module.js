'use strict';

angular.module('prep', [
	// external
	'angularUtils.directives.dirPagination',
	'ngCookies',
	'ngResource',
	'ngRoute',
	'ui.bootstrap',

	// internal
	'blogDetail',
	'blogList',
	'confirmClick',
	'login',
	'navigation',
]);