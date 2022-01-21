from django.urls import path, include
from . import views

app_name = 'ut_calendar'

urlpatterns = [
    path('', views.index, name='schedule'),
]