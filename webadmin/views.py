from django.shortcuts import render

from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from datetime import datetime, timedelta
import json
import hashlib

class Timeperiod(forms.Form):
    start = forms.DateField(label="Start", required=True)
    end = forms.DateField(label="End", required=True, )

class NewUser(forms.Form):
    name = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    email = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    password = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    teams = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))

class User:
        def __init__(self, id,name, email,CreatedAt):
            self.id = id
            self.name = name
            self.email = email  
            self.CreatedAt = CreatedAt   

class Team:
        def __init__(self,id,name):
            self.id = id
            self.name = name

class historyInstance:
    def __init__(self, user, embedded, id, timestamp):
        self.user = user
        self.embedded = embedded
        self.id = id
        self.timestamp = timestamp


class Room:
        def __init__(self,id,name, timestamp):
            self.id = id
            self.name = name
            self.timestamp = timestamp

def NewPaginator(request,list, itemsPerPage, param):

    paginator = Paginator(list, itemsPerPage)   
    page_number = request.GET.get(param) 
    page = paginator.get_page(page_number)

    return page


time = datetime.now().strftime('%H:%M')  

def index (request):

    usersTotal = 10
    roomsTotal = 33

    class Users:
        def __init__(self,usersX,usersY):
            self.usersX = usersX
            self.usersY = usersY

    usersX = ["24-09-2023", "25-09-2023","26-09-2023", "27-09-2023", "28-09-2023","29-09-2023","30-09-2023"]
    usersY = ["20","21","24","30","32","35","40"]   

    users = Users(usersX,usersY)


    return render(request, "webadmin/index.html",{    
        "usersTotal" : usersTotal,
        "roomsTotal" : roomsTotal,
        "users" : users,      
          
    })

def users (request):     

    userHistory = []
    usersList = []

    time = datetime.now().strftime('%H:%M')  


    for x in range(100):
        usersList.append(User(x,"Morten","bindzus@mail.dk",time))
        userHistory.append(historyInstance("Kronborg","Mødelokale 1",x, time))   

    user_page = NewPaginator(request,usersList,5,"userPage")
    history_page = NewPaginator(request,userHistory,9,"historyPage")
    
    if request.method == "POST":

        #HHis man har sat en dato
        timeperiodForm = Timeperiod(request.POST)
        newUser = NewUser(request.POST)

        if newUser.is_valid():

            name = newUser.cleaned_data["name"]
            email = newUser.cleaned_data["email"]
            password = newUser.cleaned_data["password"]
            teams = newUser.cleaned_data["teams"]
            print(teams)


        if timeperiodForm.is_valid():

            start = timeperiodForm.cleaned_data["start"]
            end = timeperiodForm.cleaned_data["end"]

   
    return render(request, "webadmin/users.html",{  


        "history" : userHistory,
        "users" : usersList,
        "userPage" : user_page,
        "historyPage" : history_page
        
    })

def user(request,id):

    time = datetime.now().strftime("%H:%M %D")
    currentUser = User(id,"Morten","bindzus@mail.dk",time) 
    teams = []

    userHistory = []

    for x in range(10):   
        userHistory.append(historyInstance("Kronborg","Mødelokale 1", x, time)) 

    for x in range(5):
        teams.append(Team(x,"Kantinedamerne"))

    #Pagination
    team_page = NewPaginator(request,teams,3,"teamPage")
    history_page = NewPaginator(request,userHistory,3,"userHistory")

    return render(request, "webadmin/user.html",{
        "user" : currentUser,
        "teams" : teams,
        "history": userHistory,
        "teamPage" : team_page,
        "historyPage" : history_page
    })


def rooms (request):


    rooms = []

    time = datetime.now().strftime("%H:%M %D")
    for x in range(27):   
        rooms.append(Room(x,"Mødelokale 1", time))

    
    roomsPage = NewPaginator(request,rooms,5,"roomsPage")


    return render(request, "webadmin/rooms.html",{

        "roomsPage" : roomsPage

    })

def room(request,id):


    teams = []
    history = []
    time = datetime.now().strftime("%H:%M %D")    
    room = Room(1,"Mødelokale",time)

    for x in range(23):
        teams.append(Team(x,"Kantinedamerne"))      
        history.append(historyInstance("Bruger","Dør 1",x,time))

    teamRoomsPage = NewPaginator(request,teams,5,"teamRoomsPage")
    historyPage = NewPaginator(request,history,5,"historyPage")


    return render(request, "webadmin/room.html",{

        "room" : room,
        "teams" : teams,
        "teamRoomsPage" : teamRoomsPage,
        "historyPage" : historyPage
    })

def teams(request):



    teams = []

    for x in range(33):
        teams.append(Team(x,"Køkkendamerne"))

    teamsPage = NewPaginator(request,teams,6,"teamsPage")

    return render(request, "webadmin/teams.html",{

        "teamsPage" : teamsPage

    })

def team(request,id):

    users = []
    team = Team(1,"Køkkendamerne")


    for x in range(25):

        users.append(User(x,"Morten","morten@mail.dk",time))

    teamUsersPage = NewPaginator(request,users,5,"teamUsersPage")

    return render(request, "webadmin/team.html",{

        "teamUsersPage" : teamUsersPage,
        "team" : team,
       

    })


def login(request):

    email = ""
    password = ""

    if request.method == "POST":

        email = request.POST["email_test"]
        password = request.POST["password"]

        # myobj = {'email': email, "password": password}
        # x = requests.post(url + "auth/adminlogin", json=myobj)
        # json_response = x.json()

        # token = json_response["token"]

        # session = requests.session()
        # request.session['token'] = token

        # return HttpResponseRedirect(reverse("index"))

    return render(request, "webadmin/login.html",{
        "email" : email,
        "password" : password
        
    })