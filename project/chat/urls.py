from django.urls import path, include

from . import views

urlpatterns = [
    # Chat
    path('', views.IndexView.as_view(), name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
