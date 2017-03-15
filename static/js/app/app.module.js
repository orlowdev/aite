'use strict';

angular.module('prep', [
	// external
	'angularUtils.directives.dirPagination',
	'ngResource',
	'ngRoute',
	'ui.bootstrap',

	// internal
	'blogDetail',
	'blogList',
	'confirmClick',
	'navigation',
]);