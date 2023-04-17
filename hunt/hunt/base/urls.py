from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home ,name = 'home'),
    path('home/', views.home ,name="home"),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('game/', views.game, name='game'),
    path('gamest/', views.gamest, name='gamest'),
    path('restart/', views.restart, name='restart'),
    path('winner/', views.winner,name='winner'),
    path('logout/', views.logout,name='logout'),
    path('opps/', views.opps, name='opps'),
    path('last/', views.last, name='last'),
    path('adm/', views.adm, name='adm'),
    path('usrstats/<str:pk>', views.usrstats, name='usrstats'),
    

]

handler404 = 'base.views.view404'