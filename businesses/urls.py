from django.urls import path
from businesses import views




urlpatterns = [
    path('', views.index)
]
