// navbar searchbox
$('.js-searchbox').on('click', '.icon-search, .icon-close', function (event) {
  $('.js-searchbox').toggleClass('active')
})

$('.js-searchbox input').keydown(function (event) {
  // press enter
  if (event.keyCode === 13) location.href = '/search/?q=' + $(this).val()
});



$('.js-slick').each(function () {
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



$('.js-tgee-dropdown > .tgee-dropdown-trigger').click(function (event) {
  $(this).parent('.js-tgee-dropdown').toggleClass('active');
  event.stopPropagation()
})

$('.js-mobile-toggle-menu > .toggle-trigger').click(function (event) {
  $('.js-mobile-toggle-menu').toggleClass('active')
  event.stopPropagation()
})

$('body').click(function () {
  $('.js-tgee-dropdown').removeClass('active')
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


const team_data = {
  description: '2012 年，一群懷抱著遊戲夢的年輕人，在 18 樓合租宿舍結成團隊；三年後，以《麥克尼西亞》斬獲多座大獎的這群夥伴，正式成立光穹遊戲股份有限公司 (18Light Game Ltd.)，並獨立開發《螢幕判官》這款曾獲東南亞國際行動遊戲大賽 (IMGA SEA) 等海內外獎項肯定的劇情遊戲。隨後更與出版社異業合作，推出《螢幕判官》同名小說與設定集，另由發行商發行任天堂 Switch 版本，朝著把臺灣作品推向國際的目標穩步向前。結合公司名稱的諧音單字「聚光燈」，光穹遊戲以「Spotlights Yourself.」作為核心理念，致力開發聚焦於玩家的高品質遊戲。我們認為，每場遊戲最獨特的體驗、就是玩家們親手創造的回憶；因此，我們期許能專注於每一位玩家本身，打造兼具遊玩樂趣與情感連結的作品，藉由與遊戲內容相互輝映的劇情，使玩家們彷彿身歷其境般盡情探索、對遊戲內的世界更感同身受。透過遊戲，光穹將與你一同踏上漫長的冒險旅程，難以取代的故事。',
  rewards: ['2019 最佳創新獎 - 數位內容產品獎 ', '2019 最佳創新獎 - 數位內容產品獎 ', '2019 最佳創新獎 - 數位內容產品獎 '],
  links: [
    {text: '《螢幕判官》開發團隊新作《棄海：波弟大冒險》正式揭曉 即日起開放預先登錄 - GNN 記者 Jessica 報導', href: 'https://xd.adobe.com/view/ae19e307-50e9-41f4-90d5-8d10bc5136e3-fb4a' },
    {text: '《螢幕判官》開發團隊新作《棄海：波弟大冒險》正式揭曉 即日起開放預先登錄 - GNN 記者 Jessica 報導', href: 'https://xd.adobe.com/view/ae19e307-50e9-41f4-90d5-8d10bc5136e3-fb4a' },
  ]
}

new Vue({
  el: '#vue-team-reward',
  data: {
    description_editing: false,
    rewards_editing: false,
    links_editing: false,
    team_data: JSON.parse(JSON.stringify(team_data)),
    form_data: JSON.parse(JSON.stringify(team_data)),
  },
  methods: {
    save_description: function () {
      this.description_editing = false
      this.team_data.description = this.form_data.description
    },
    save_rewards: function () {
      this.rewards_editing = false
      this.team_data.rewards = JSON.parse(JSON.stringify(this.form_data.rewards))
    },
    save_links: function () {
      this.links_editing = false
      this.team_data.links = JSON.parse(JSON.stringify(this.form_data.links))
    },
    cancel: function () {
      this.description_editing = false
      this.rewards_editing = false
      this.links_editing = false
      this.form_data = JSON.parse(JSON.stringify(this.team_data))
    }
  },
  delimiters: ['[[',']]'],
})








$('#js-games-gallary').on('click', '.js-game-show', function (event){
  event.stopPropagation()
  $('#modal_game_show').modal('show')
})

$('#js-games-gallary').on('click', '.js-game-edit', function (event){
  event.stopPropagation()
  $('#modal_game_edit').modal('show')
});

