from django.urls import path
from businesses import views




urlpatterns = [
    path('', views.index),
    path('auth/', views.auth_page),
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('logout/', views.logout_view),
    path('create-store/', views.create_store),
]
