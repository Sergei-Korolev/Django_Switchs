from django.urls import path
from .import views

app_name = "switchs"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:switch_id>/detail', views.detail, name='detail'),
]
