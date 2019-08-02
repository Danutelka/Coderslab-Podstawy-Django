 
from django.conf.urls import url
from django.contrib import admin
from django.urls import re_path, path
from random import randint
from edu.views import show_number
from edu.views import hello
from edu.views import random1
from edu.views import random_max
from edu.views import random_max_min
from edu.views import hello_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/<int:number>', show_number),
    path('hello/', hello),
    path('random', random1),
    # path('random/<int:number>', random_max),
    re_path(r'^random/(?P<number>(\d){2,4})/$', random_max),
    # path('random/<int:min_number>/<int:max_number>', random_max_min),
    re_path(r'^random/(?P<min_number>(\d){2})/(?P<max_number>(\d){4})/$', random_max_min),
    # path('hello/<str:name>', hello_user)
    re_path(r'^hello/(?P<name>(^[A-Z][a-z]+))/$', hello_user)
]
