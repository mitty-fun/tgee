


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



new Vue({
  el: '#vue-team-reward',
  data: {
    rewards_editing: false,
    links_editing: false,
    rewards: ['2019 最佳創新獎 - 數位內容產品獎 ', '2019 最佳創新獎 - 數位內容產品獎 ', '2019 最佳創新獎 - 數位內容產品獎 '],
    links: [
      {text: '《螢幕判官》開發團隊新作《棄海：波弟大冒險》正式揭曉 即日起開放預先登錄 - GNN 記者 Jessica 報導', href: 'https://xd.adobe.com/view/ae19e307-50e9-41f4-90d5-8d10bc5136e3-fb4a' },
      {text: '《螢幕判官》開發團隊新作《棄海：波弟大冒險》正式揭曉 即日起開放預先登錄 - GNN 記者 Jessica 報導', href: 'https://xd.adobe.com/view/ae19e307-50e9-41f4-90d5-8d10bc5136e3-fb4a' },
    ]
  },
  delimiters: ['[[',']]'],
})