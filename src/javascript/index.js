const $ = require('jquery')
require('bootstrap')
require('../../node_modules/slick-carousel/slick/slick')


$('.js-slick').slick({
  dots: true,
  speed: 300,
  slidesToShow: 1,
  nextArrow: '.next-arrow',
  prevArrow: '.prev-arrow',
  appendDots: '.dots',
  fade: true
});


$('.js-toggle-searchbox').click(function () {
  $(this).parent().toggleClass('active');
});

$('.js-tgee-dropdown > .tgee-dropdown-trigger').click(function () {
  $(this).parent('.js-tgee-dropdown').toggleClass('active');
})