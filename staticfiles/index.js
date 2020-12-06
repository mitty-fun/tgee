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
  });
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


// 客製化下拉選單
(function () {
  $('.js-tgee-select').each(function () {

    var el_root = $(this)
    var el_select = $(this).find('select')
    var el_default_text = $(this).find('.default-text')
    var el_options = $(this).find('option:not(".default-text")')
    var el_trigger = $('<div class="tgee-dropdown-trigger"></div>')
    var el_trigger_text = $('<span class="mr-auto"></span>')
    var el_trigger_icon = $('<i class="fas fa-chevron-down"></i>')
    var el_dropdown_menu = $('<div class="tgee-dropdown-menu"></div>')
    var el_dropdown_menu_body = $('<div class="tgee-dropdown-menu-body"></div>')

    el_trigger_text.text(el_default_text.text())
    el_trigger.append(el_trigger_text)
    el_trigger.append(el_trigger_icon)
    el_dropdown_menu.append(el_dropdown_menu_body)
    el_root.append(el_trigger)
    el_root.append(el_dropdown_menu)
    
    el_options.each(function () {
      var el = $('<p class="tgee-dropdown-item"></p>')
      var value = $(this).val()
      var text = $(this).text()
      el.text(text)
      el.data('value', value)

      function onclick() {
        el_select.val(value)
        el_trigger_text.text(text)
      }
      el.click(onclick)
      el_dropdown_menu_body.append(el)
    })

    $(el_select).hide()

    el_trigger.click(function (event) {
      $(el_root).toggleClass('active')
      event.stopPropagation()
    });
    
    $('body').click(function () {
      $(el_root).removeClass('active')
    })
  });
})();


//客製化下拉多選單
(function () {
  $('.js-tgee-select-multi').each(function () {
    
    var el_root = $(this)
    var el_trigger = $(this).find('.tgee-dropdown-trigger')
    var el_trigger_text = el_trigger.find('span')
    var el_dropdown_menu = $(this).find('.tgee-dropdown-menu')
    var inputs = $(this).find('input')

    inputs.on('change', function () {
      var texts = []
      inputs.each(function () {
        if (this.checked) texts.push($(this).val())
      })

      if (texts.length > 3) {
        texts.length = 3
        texts.push('...')
      }
      if (texts.length == 0) texts.push('平台')
      el_trigger_text.text(texts.join(', '))
    })
    
    el_trigger.click(function (event) {
      el_root.toggleClass('active')
      event.stopPropagation()
    })

    el_dropdown_menu.click(function (event) {
      event.stopPropagation()
    })

    $('body').click(function () {
      $(el_root).removeClass('active')
    })
  })
})();