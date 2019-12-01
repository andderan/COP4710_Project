from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Teams/', views.Teams, name='Teams'),
    path('Teams/<int:Team_Int_Key>/', views.TeamDisplay, name='TeamDisplay'),
    path('Matches/', views.Matches, name='Matches'),
    path('Matches/<int:Match_Id>/', views.MatchDisplay, name='MatchDisplay')
]
