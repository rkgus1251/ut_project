from django.urls import path, include
from . import views

app_name = 'ut_calendar'

urlpatterns = [
    path('', views.index, name='schedule_list'),
    path('<int:date_id>/', views.detail, name='schedule_detail'),
    path('create/', views.schedule_create, name='schedule_create'),
    path('calendar/', views.ex),
]