from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path("users", views.users, name="users"),
    path("user/<int:id>", views.user, name="user"),
    path("deleteuser", views.deleteuser, name="deleteuser"),
    path("edituser", views.edituser, name="edituser"),
    path("editroom", views.editroom, name="editroom"),
    path("rooms", views.rooms, name="rooms"),
    path("deleteroom", views.deleteroom, name="deleteroom"),  
    path("room/<int:id>", views.room, name="room"),
    path("teams",views.teams, name="teams"),
    path("team/<int:id>", views.team, name="team"),
    path("deleteteam", views.deleteteam, name="deleteteam"),
    path("editteam", views.editteam, name="editteam"),
    path("teamsaddusers", views.teamsaddusers, name="teamsaddusers"), 
    path("teamsdeleteusers", views.teamsdeleteusers, name="teamsdeleteusers"),   
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    
    
]