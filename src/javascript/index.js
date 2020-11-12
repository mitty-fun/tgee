const $ = require('jquery')
const Vue = require('vue')

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

$('.js-mobile-toggle-menu > .toggle-trigger').click(function () {
  $('.js-mobile-toggle-menu').toggleClass('active')
})


new Vue({
  el: '.js-vue-imgs-uploader',
  data: {
    images: [
      { id: 0, src: undefined },
      { id: 0, src: 'images/examples/1.jpg' },
      { id: 0, src: 'images/examples/2.jpg' },
      { id: 0, src: 'images/examples/3.jpg' },
      { id: 0, src: 'images/examples/4.jpg' },
      { id: 0, src: 'images/examples/5.jpg' },
      { id: 0, src: 'images/examples/6.jpg' },
    ]
  },
  methods: {
    update_image: function (index, e) {

      var input = e.target;
      if (input.files && input.files[0]) {
        var reader = new FileReader();

        var self = this;

        reader.onload = function (e) {
          self.images[index].src = e.target.result;

          if (index == 0) self.images.unshift({id: 0, src: undefined})
        };

        reader.readAsDataURL(input.files[0]);
      }
      
    }
  }
})



