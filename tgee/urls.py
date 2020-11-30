from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [

    path('', views.index, name='home'),

    path('news/', views.news, name='news'),
    path('news/game/', views.news_game, name='news_game'),
    path('news/official/', views.news_official, name='news_official'),
    path('news/market/', views.news_market, name='news_market'),

    path('articles/', views.articles, name='articles'),
    path('articles/manage', views.articles_manage, name='articles_manage'),
    path('articles/<str:hash_id>/show/', views.articles_show, name='articles_show'),

    path('campaigns/', views.campaigns, name='campaigns'),
    path('campaigns/courses/', views.campaigns_courses, name='campaigns_courses'),
    path('campaigns/<str:hash_id>/show/', views.campaigns_show, name='campaigns_show'),

    path('service/', views.service, name='service'),
    path('service_logged_in/', views.service_logged_in, name='service_logged_in'),

    path('teams/<str:name>/show/', views.teams_show, name='teams_show'),

    path('games/', views.games, name='games'),
    path('games/<str:hash_id>/edit/', views.games_edit, name='games_edit'),

    path('resources/', views.resources, name='resources'),
    path('resources/accounting', views.resources_accounting, name='resources_accounting'),
    path('resources/community', views.resources_community, name='resources_community'),
    path('resources/competition', views.resources_competition, name='resources_competition'),
    path('resources/government', views.resources_government, name='resources_government'),

    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),

    path('our/privacy/', views.privacy, name='privacy'),
    path('our/terms/', views.terms, name='terms'),
    path('our/faq/', views.faq, name='faq'),

    path('user/login/', views.login, name='login'),
    path('user/email_valid/', views.email_valid, name='email_valid'),
    path('user/reset_password/', views.reset_password, name='reset_password'),
    path('user/reset_password_success/', views.reset_password_success, name='reset_password_success'),
    path('user/signup_premium_review/', views.signup_premium_review, name='signup_premium_review'),
    path('user/signup_premium/', views.signup_premium, name='signup_premium'),
    path('user/signup/', views.signup, name='signup'),

    path('user/email/', views.email, name='email'),

    path('404/', views.not_found, name='404'),
]