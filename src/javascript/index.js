const $ = require('jquery')
require('bootstrap')
require('../../node_modules/slick-carousel/slick/slick')


$('.js-slick').each(function () {
  console.log($(this).data('slides-to-show'))
  $(this).slick({
    dots: true,
    speed: 300,
    slidesToShow: $(this).data('slides-to-show') || 1,
    nextArrow: $(this).next().find('.next-arrow'),
    prevArrow: $(this).next().find('.prev-arrow'),
    appendDots: $(this).next().find('.dots'),
    // fade: true
  });
})

$('.js-toggle-searchbox').click(function () {
  $(this).parent().toggleClass('active');
});

$('.js-tgee-dropdown > .tgee-dropdown-trigger').click(function () {
  $(this).parent('.js-tgee-dropdown').toggleClass('active');
})