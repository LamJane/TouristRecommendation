from django.urls import path
from TRlogin import views

urlpatterns = [
    path('',views.shouye,name='shouye'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout')
]