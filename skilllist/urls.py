from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^generateImage$', views.generateImage, name='generateImage'),
    url(r'^$', views.skill_list, name='skill_list'),
    url(r'^asheron$', views.asheron, name='asheron'),
    url(r'^marjory$', views.marjory, name='marjory'),
]