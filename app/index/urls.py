from django.urls import path
from . import views


urlpatterns = [
  path('bot_list/', views.botList, name='bot_list'),
  path('', views.index, name='index'),
]
