from django.shortcuts import render, redirect

# 遊戲
# 圖片路徑, 標題, 內文, 標籤
games_data = [
    ( 'games/1.jpg', '赤燭遊戲', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》...', ['恐怖', 'Block Making RPG'] ),
    ( 'games/2.jpg', '人生畫廊', '不簡單的操作模式。以一幅幅的畫作代一款詭異插畫風的 2D 解謎手機遊戲，藉由點擊、滑動簡單的操作功能創造...', ['恐怖', 'Block Making RPG'] ),
    ( 'games/3.jpg', '沈默意志', '一款 PC  2D 橫向對話敘事類遊戲。一部黑暗的未來寓言，一場撼動人性的冒險，一次沈浸的電影式遊戲體驗。...', ['恐怖', 'Block Making RPG'] ),
    ( 'games/4.jpg', '守夜人：長夜', '一款 2D 橫向捲軸動作遊戲，故事世界觀融入克蘇魯神話陰暗又神秘背景。遊戲中玩家將扮演在夜裡醒來失憶的主...', ['恐怖', 'Block Making RPG'] ),
    ( 'games/1.jpg', 'ALIISHA', '由兩名玩家分別扮演沒有痛覺的姊姊 Aisha，與沒有情感的妹妹 Lisha，玩家必須透過各自的能力，同時還要互相溝...', ['恐怖', 'Block Making RPG'] ),
    ( 'games/2.jpg', '動物森友會', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》...', ['恐怖', 'Block Making RPG'] ),
    ( 'games/3.jpg', '赤燭遊戲', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》...', ['恐怖', 'Block Making RPG'] ),
    ( 'games/4.jpg', '人生畫廊', '不簡單的操作模式。以一幅幅的畫作代一款詭異插畫風的 2D 解謎手機遊戲，藉由點擊、滑動簡單的操作功能創造...', ['恐怖', 'Block Making RPG'] ),
    ( 'games/1.jpg', '沈默意志', '一款 PC  2D 橫向對話敘事類遊戲。一部黑暗的未來寓言，一場撼動人性的冒險，一次沈浸的電影式遊戲體驗。...', ['恐怖', 'Block Making RPG'] )
]

# 遊戲團隊
team = {
    'img': 'team/cover.jpg',
    'name': '赤竹遊戲',
    'author': '陳任軒',
    'contact': '0900-000-000',
    'email': 'pr@18light.cc',
    'city': '台北市',
    'year': '2012',
    'site': 'https://www.18light.cc',
    'content': '2012 年，一群懷抱著遊戲夢的年輕人，在 18 樓合租宿舍結成團隊；三年後，以《麥克尼西亞》斬獲多座大獎的這群夥伴，正式成立光穹遊戲股份有限公司 (18Light Game Ltd.)，並獨立開發《螢幕判官》這款曾獲東南亞國際行動遊戲大賽 (IMGA SEA) 等海內外獎項肯定的劇情遊戲。隨後更與出版社異業合作，推出《螢幕判官》同名小說與設定集，另由發行商發行任天堂 Switch 版本，朝著把臺灣作品推向國際的目標穩步向前。結合公司名稱的諧音單字「聚光燈」，光穹遊戲以「Spotlights Yourself.」作為核心理念，致力開發聚焦於玩家的高品質遊戲。我們認為，每場遊戲最獨特的體驗、就是玩家們親手創造的回憶；因此，我們期許能專注於每一位玩家本身，打造兼具遊玩樂趣與情感連結的作品，藉由與遊戲內容相互輝映的劇情，使玩家們彷彿身歷其境般盡情探索、對遊戲內的世界更感同身受。透過遊戲，光穹將與你一同踏上漫長的冒險旅程，難以取代的故事。',
    'rewords': ['2019 最佳創新獎 - 數位內容產品獎 ', '2019 銀獎 - 遊戲之星選拔賽', '2019 最佳手機遊戲 - Indie Game Award'],
    'news': ['《螢幕判官》開發團隊新作《棄海：波弟大冒險》正式揭曉 即日起開放預先登錄 - GNN 記者 Jessica 報導'],
    'member_images': ['team/members.jpg', 'team/members.jpg', 'team/members.jpg', 'team/members.jpg'],
    'games': games_data[0:6],
}


game_data = {
    'imgs': ['games/1.jpg', 'games/2.jpg', 'games/3.jpg', 'games/4.jpg', 'games/5.jpg'],
    'title_zh': '赤燭遊戲',
    'title_en': 'red candle game',
    'participants': 3,
    'video': 'https:/www.com.tw/',
    'website': 'https:/www.com.tw/',
    'content_zh': '2012 年，一群懷抱著遊戲夢的年輕人，在 18 樓合租宿舍結成團隊；三年後，以《麥克尼西亞》斬獲多座大獎的這群夥伴，正式成立光穹遊戲股份有限公司 (18Light Game Ltd.)，並獨立開發《螢幕判官》這款曾獲東南亞國際行動遊戲大賽 (IMGA SEA) 等海內外獎項肯定的劇情遊戲。隨後更與出版社異業合作，推出《螢幕判官》同名小說與設定集，另由發行商發行任天堂 Switch 版本，朝著把臺灣作品推向國際的目標穩步向前。結合公司名稱的諧音單字「聚光燈」，光穹遊戲以「Spotlights Yourself.」作為核心理念，致力開發聚焦於玩家的高品質遊戲。我們認為，每場遊戲最獨特的體驗、就是玩家們親手創造的回憶；因此，我們期許能專注於每一位玩家本身，打造兼具遊玩樂趣與情感連結的作品，藉由與遊戲內容相互輝映的劇情，使玩家們彷彿身歷其境般盡情探索、對遊戲內的世界更感同身受。透過遊戲，光穹將與你一同踏上漫長的冒險旅程，難以取代的故事。',
    'content_en': 'In 2012, a group of young people with game dreams formed a team in the shared dormitory on the 18th floor. Three years later, the group of partners who won multiple awards with "Mcnicia" formally established 18Light Game Co., Ltd. Ltd.), and independently developed "The Screen Judge", a story game that has won awards at home and abroad such as IMGA SEA. Later, he cooperated with publishing houses in different industries to launch a novel and set of "The Screen Judge" with the same name. The publisher also released the Nintendo Switch version, moving forward steadily towards the goal of promoting Taiwanese works internationally. Combining the homophonic word "Spotlight" of the company name, Light Dome Games takes "Spotlights Yourself." as its core concept and is committed to developing high-quality games that focus on players. We believe that the most unique experience of each game is the memories created by the players. Therefore, we hope to focus on each player and create works that are both fun and emotionally connected to each other by reflecting on the game content. The plot of the game allows players to explore as if they are immersed in the environment, and feel more empathetic to the world in the game. Through the game, Light Dome will embark on a long adventure with you, an irreplaceable story.',
    'languages': ['繁中'],
    'platforms': ['其他'],
    'types': ['恐怖'],
}

# 相關資源
# 圖片路徑, 標題, 地區, 時間, 標籤
resources_data = [
    ('resources/1@2x.jpg', '遊戲創業及啟動基金', '全國性', '2020-21-08', ['學生']),
    ('resources/2@2x.jpg', '遊戲創業及啟動基金', '全國性', '2020-21-08', ['學生']),
    ('resources/2@2x.jpg', '遊戲創業及啟動基金', '全國性', '2020-21-08', ['學生']),
    ('resources/1@2x.jpg', '遊戲創業及啟動基金', '全國性', '2020-21-08', ['學生']),
    ('resources/1@2x.jpg', '遊戲創業及啟動基金', '全國性', '2020-21-08', ['學生']),
    ('resources/2@2x.jpg', '遊戲創業及啟動基金', '全國性', '2020-21-08', ['學生']),
    ('resources/2@2x.jpg', '遊戲創業及啟動基金', '全國性', '2020-21-08', ['學生']),
    ('resources/1@2x.jpg', '遊戲創業及啟動基金', '全國性', '2020-21-08', ['學生']),
]

# 新聞
# 圖片路徑, 標題
news_data = [
    ('news/1.svg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('news/2.svg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('news/3.svg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('news/2.svg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('news/3.svg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('news/1.svg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('news/3.svg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('news/1.svg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('news/2.svg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
]

# 活動
# 圖片路徑, 標題
campaigns_data = [
    ('campaigns/1.jpg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('campaigns/2.jpg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('campaigns/3.jpg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('campaigns/4.jpg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('campaigns/1.jpg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('campaigns/2.jpg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('campaigns/3.jpg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('campaigns/4.jpg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
    ('campaigns/1.jpg', '創作者的生存遊戲 #1畢業後，如何集體創作並...'),
]

#常見問題
faq_data = [
 ('關於創夢市集', '創夢市集由網銀國際、遊戲橘子、華義國際、昱泉國際、齊民等五大遊戲業者及新光金國際創投共同出資成立。2017 年起集中資源，成立台灣第一個聚焦於「娛樂 X 生活」領域且提供早期投資的新創加速器。三年來共加速超過 65 家新創團隊，並完成超過 20 案早期投資。' ),  
 ('關於創夢市集', '創夢市集由網銀國際、遊戲橘子、華義國際、昱泉國際、齊民等五大遊戲業者及新光金國際創投共同出資成立。2017 年起集中資源，成立台灣第一個聚焦於「娛樂 X 生活」領域且提供早期投資的新創加速器。三年來共加速超過 65 家新創團隊，並完成超過 20 案早期投資。' ),  
 ('關於創夢市集', '創夢市集由網銀國際、遊戲橘子、華義國際、昱泉國際、齊民等五大遊戲業者及新光金國際創投共同出資成立。2017 年起集中資源，成立台灣第一個聚焦於「娛樂 X 生活」領域且提供早期投資的新創加速器。三年來共加速超過 65 家新創團隊，並完成超過 20 案早期投資。' ),  
 ('關於創夢市集', '創夢市集由網銀國際、遊戲橘子、華義國際、昱泉國際、齊民等五大遊戲業者及新光金國際創投共同出資成立。2017 年起集中資源，成立台灣第一個聚焦於「娛樂 X 生活」領域且提供早期投資的新創加速器。三年來共加速超過 65 家新創團隊，並完成超過 20 案早期投資。' ),  
 ('關於創夢市集', '創夢市集由網銀國際、遊戲橘子、華義國際、昱泉國際、齊民等五大遊戲業者及新光金國際創投共同出資成立。2017 年起集中資源，成立台灣第一個聚焦於「娛樂 X 生活」領域且提供早期投資的新創加速器。三年來共加速超過 65 家新創團隊，並完成超過 20 案早期投資。' ),  
]

#文章
articles_data = [
    ('遊戲新聞', '文章標題文章標題文章標題文，章標題文標題文...', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》隔著螢幕，誰是判官？以媒體識讀與輿論殺...'),
    ('遊戲新聞', '文章標題文章標題文章標題文，章標題文標題文...', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》隔著螢幕，誰是判官？以媒體識讀與輿論殺...'),
    ('遊戲新聞', '文章標題文章標題文章標題文，章標題文標題文...', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》隔著螢幕，誰是判官？以媒體識讀與輿論殺...'),
    ('遊戲新聞', '文章標題文章標題文章標題文，章標題文標題文...', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》隔著螢幕，誰是判官？以媒體識讀與輿論殺...'),
    ('遊戲新聞', '文章標題文章標題文章標題文，章標題文標題文...', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》隔著螢幕，誰是判官？以媒體識讀與輿論殺...'),
]

search_data = [
    ('遊戲新聞', '文章標題文章標題文章標題文文章標題文章標題文章標題文', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》隔著螢幕，誰是判官？以媒體識讀與輿論殺...'),
    ('遊戲新聞', '文章標題文章標題文章標題文文章標題文章標題文章標題文', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》隔著螢幕，誰是判官？以媒體識讀與輿論殺...'),
    ('遊戲新聞', '文章標題文章標題文章標題文文章標題文章標題文章標題文', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》隔著螢幕，誰是判官？以媒體識讀與輿論殺...'),
    ('遊戲新聞', '文章標題文章標題文章標題文文章標題文章標題文章標題文', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》隔著螢幕，誰是判官？以媒體識讀與輿論殺...'),
    ('遊戲新聞', '文章標題文章標題文章標題文文章標題文章標題文章標題文', '隔著螢幕，誰是判官？以媒體識讀與輿論殺人等社會議題為主軸、上市以來廣受好評的臺灣原創遊戲《螢幕判官》隔著螢幕，誰是判官？以媒體識讀與輿論殺...'),
]

filter_options = [
    '互動戲劇', '動作冒險', '休閒', '動作角色扮演', 
    '角色扮演', '第一人稱射擊', '音樂', '音樂節奏',
    '運動', '策略角色扮演', '桌上遊戲', '模擬',
    '家庭', '模擬角色扮演', '射擊', '戰略',
    '恐怖', '獨特遊戲', '格鬥', '賽車',
    '益智', '動作', '其他',
]

# 相關資源
def resources(request):
    return redirect('resources_competition')

# 會計法務
def resources_accounting(request):
    return render(request, 'resources/accounting.html', { 'resources': resources_data })

# 遊戲社群
def resources_community(request):
    return render(request, 'resources/community.html', { 'resources': resources_data })

# 競賽獎項
def resources_competition(request):
    return render(request, 'resources/competition.html', { 'resources': resources_data })

# 政府計畫
def resources_government(request):
    return render(request, 'resources/government.html', { 'resources': resources_data })



# 首頁
def index(request):
    data = {
        'news': news_data[0:3],
    }
    return render(request, 'index.html', data)

# 關於我們
def about(request):
    return render(request, 'about.html')

# 隱私權政策
def privacy(request):
    return render(request, 'our/privacy.html')

# 版權說明
def terms(request):
    return render(request, 'our/terms.html')

# 常見問題
def faq(request):
    return render(request, 'our/faq.html', {'faq_data': faq_data, 'filter_options': filter_options})

# 活動列表
def campaigns(request):
    return render(request, 'campaigns/index.html', {'campaigns': campaigns_data})

# 課程活動
def campaigns_courses(request):
    return render(request, 'campaigns/courses.html', {'campaigns': campaigns_data})

# 活動檢視
def campaigns_show(request, hash_id):
    return render(request, 'campaigns/show.html', {'campaigns': campaigns_data[0:2]})

# 專屬服務(未登入)
def service(request):
    return render(request, 'service.html')

# 專屬服務(登入)
def service_logged_in(request):
    data = {
        'campaigns': campaigns_data,
        'resources': resources_data,
    }
    return render(request, 'service_logged_in.html', data)

# 團隊編輯
def teams_show(request, name):
    data = {
        'team': team,
        'news': news_data[0:3],
        'game': game_data,
    }
    return render(request, 'teams/show.html', data)

# 新聞
def news(request):
    return redirect('news_official')

# 產業新聞
def news_market(request):
    return render(request, 'news/market.html', { 'posts': news_data })

# 官方新聞
def news_official(request):
    return render(request, 'news/official.html', { 'posts': news_data })

# 遊戲新聞
def news_game(request):
    return render(request, 'news/game.html', { 'posts': news_data })

# 遊戲列表
def games(request):
    return render(request, 'games/index.html', {'games': games_data, 'filter_options': filter_options})

# 遊戲編輯
def games_edit(request, hash_id):
    return render(request, 'games/edit.html')

# 知識文章
def articles(request):
    return render(request, 'articles/index.html', { 'posts': news_data })

# 文章檢視
def articles_show(request, hash_id):
    return render(request, 'articles/show.html', { 'news': news_data[0:3], 'aritcle': news_data[0] })

# 文章慣例
def search(request):
    return render(request, 'search.html', {'search': search_data})

# 404
def not_found(request):
    return render(request, '404.html')
# 登入
def login(request):
    return render(request, 'user/login.html')

# 重設密碼
def reset_password(request):
    return render(request, 'user/reset_password.html')

# 重設密碼成功
def reset_password_success(request):
    return render(request, 'user/reset_password_success.html')

# 進階註冊完成
def signup_premium_review(request):
    return render(request, 'user/signup_premium_review.html')

# 進階註冊
def signup_premium(request):
    return render(request, 'user/signup_premium.html')

# 註冊
def signup(request):
    return render(request, 'user/signup.html')

# email
def email(request):
    return render(request, 'user/email.html')