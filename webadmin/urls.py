from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),

    #Main pages
    path("users", views.users, name="users"),
    path("rooms", views.rooms, name="rooms"),
    path("teams",views.teams, name="teams"),
    path("permissions", views.permissions, name="permissions"),

    #API calls
    #User
    path("deleteuser", views.deleteuser, name="deleteuser"),
    path("edituser", views.edituser, name="edituser"),
    path("usersdeleteteam", views.usersdeleteteam, name="usersdeleteteam"),
    path("usersaddteam", views.usersaddteam, name="usersaddteam"),
    #Room
    path("editroom", views.editroom, name="editroom"),    
    path("deleteroom", views.deleteroom, name="deleteroom"),  
    #Team
    path("deleteteam", views.deleteteam, name="deleteteam"),
    path("editteam", views.editteam, name="editteam"),
    path("teamsaddusers", views.teamsaddusers, name="teamsaddusers"), 
    path("teamsdeleteusers", views.teamsdeleteusers, name="teamsdeleteusers"),   
    #Permission
    path("deletepermission", views.deletepermission, name="deletepermission"),
    path("editpermission", views.editpermission, name="editpermission"),

    #Login/Logout
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),

    #Unit test example
    # path("test", views.test_example, name="example")

    
    #Sub pages
    # path("user/<int:id>", views.user, name="user"),
    # path("room/<int:id>", views.room, name="room"),    
    # path("team/<int:id>", views.team, name="team"),
    
    
]
