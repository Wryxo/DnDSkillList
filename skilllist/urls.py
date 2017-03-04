from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.skill_list, name='skill_list'),
    url(r'^asheron$', views.asheron, name='asheron'),
]