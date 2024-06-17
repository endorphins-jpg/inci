/// <reference path="helpers_brasa.js" />
'use strict';

onClick('#toggle-btn', function () {
    $('#sidebar').toggleClass('expand')
    $(this).toggleClass('rotate')
})