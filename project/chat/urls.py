from django.urls import path, include

from . import views

urlpatterns = [
    # Chat
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    # Auth
    path('accounts/', include('django.contrib.auth.urls')),
]
