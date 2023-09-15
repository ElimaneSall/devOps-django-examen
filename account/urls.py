from django.urls import path

from .views import signup, login_user, logout_user, liste_utilisateurs, visites

urlpatterns =[
    path('signup', signup, name='signup'),
    path('login', login_user, name='login_user'),
    path('logout', logout_user, name='logout'),
    path('liste-utilisateurs/', liste_utilisateurs, name='liste-utilisateurs'),
    path('visites/', visites, name='visites'),
]