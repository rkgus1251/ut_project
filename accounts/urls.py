from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', auth_views.LogoutView.as_view(), name='signout'),
    path('find_username/', views.find_username, name='find_username'),
    path('signin/kakao/', views.kakao_login, name="kakao_signin"),
    path('signin/kakao/callback/', views.kakao_login_callback, name="kakao_signin_callback"),
]