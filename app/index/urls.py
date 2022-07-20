from django.urls import path
from . import views


urlpatterns = [
  path('bot_list/', views.botList, name='bot_list'),
  path('message/new', views.message_new, name='message_new'),
  path('', views.index, name='index'),
]
