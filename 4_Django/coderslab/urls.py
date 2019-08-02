"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from exercises.views import show_article
from exercises.views import show_band
from homework.views import movies
# from homework.views import show_movie
from homework.views import movie_detail
from homework.views import all_persons
from homework.views import person_detail
# from homework.views import edit_person
from homework.views import person_add
from homework.views import person_edit
from homework.views import search_movie
from football.views import league_table
from football.views import games_played
from exercises.views import range_view
from exercises.views import tabliczka_mnozenia_view
from exercises.views import witaj
from exercises.views import temperatura
from exercises.views import setSession
from exercises.views import showSession 
from exercises.views import delSession
from exercises.views import login
from exercises.views import addToSession
from exercises.views import showAllSession
from exercises.views import setCookie
from exercises.views import showCookie
from exercises.views import delCookie
from exercises.views import addToCookie
from exercises.views import showAllCookies


urlpatterns = [
    path('admin', admin.site.urls),
    url(r'article/(?P<id>(\d)+)/$', show_article),
    url(r'show_band/(?P<id>(\d)+)/$', show_band),
    path('movies', movies),
    url (r'movie_detail/(?P<id>(\d)+)/$', movie_detail),
    path('persons', all_persons),
    url(r'person_detail/(?P<id>(\d)+)/$', person_detail),
    # path('edit_person/<int:person_id>', edit_person),
    path('add', person_add),
    url(r'person_edit/(?P<id>(\d)+)/$', person_edit),
    path('szukanie', search_movie),
    path('table', league_table),
    path('games', games_played),
    path('range', range_view),
    path('tablica', tabliczka_mnozenia_view),
    path('witaj', witaj),
    path('temp', temperatura),
    path('setSession', setSession),
    path('showSession', showSession),
    path('delSession', delSession),
    path('login', login), 
    path('addToSession', addToSession),
    path('showAllSession', showAllSession),
    path('setCookie', setCookie),
    path('showCookie', showCookie),
    path('delCookie', delCookie),
    path('addToCookie', addToCookie), 
    path('showAllCookies', showAllCookies),

]
