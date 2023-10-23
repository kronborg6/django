from django.shortcuts import render

from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from datetime import datetime, timedelta
import json
import hashlib
import requests

class NewUser(forms.Form):
    name = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    email = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    teams = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))

class NewPermission(forms.Form):    
    users = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    rooms = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    teams = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    days = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    startDate = forms.DateField()
    endDate = forms.DateField()
    startTime = forms.CharField()
    endTime = forms.CharField()


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

api_url = "https://api.seaofkeys.com"


def usersAmount(itemList):
     
    for i, item in enumerate(itemList):
        itemList[i]["totalUsers"] = len(item["users"])

    return itemList

def GetAPI(endpoint, request):

    session_cookies = request.session.get('token')    

    if session_cookies:
        x = requests.get(api_url + endpoint, cookies=session_cookies)
        return x    

def PostAPI(endpoint, obj,request):

    session_cookies = request.session.get('token')  

    x = requests.post(api_url + endpoint,json=obj, cookies=session_cookies)
    return x


def ReplaceCommas(item):
    
    if item[-1] == ",":
         
        item = item[:-1] + ""

    if item == ".":

        item = None 
    
    elif "," not in item:
         
        item = int(item)   

    return item  

def index (request):
    
    if request.session.get("token") == None:            
            return redirect("/login")    

    usersTotal = GetAPI("/stats/users",request).json()["user_count"]
    roomsTotal = GetAPI("/stats/rooms",request).json()["user_count"]
    teamsTotal = GetAPI("/stats/teams",request).json()["user_count"]
    
    class Users:
        def __init__(self,usersX,usersY):
            self.usersX = usersX
            self.usersY = usersY

    usersX = ["16-10-2023", "17-10-2023","18-10-2023", "19-10-2023", "20-10-2023","21-10-2023","22-10-2023"]
    usersY = ["20","21","24","30","32","35","40"]   
    users = Users(usersX,usersY)

    return render(request, "webadmin/index.html",{    
        "usersTotal" : usersTotal,
        "roomsTotal" : roomsTotal,
        "teamsTotal" : teamsTotal,
        "users" : users, 
          
    })
    

def GetTeams(result):
     
    teams = list()      

    for item in result:
        instance = {"id" : item["id"], "name" : item["name"]}
        teams.append(instance)  

    return teams

def GetUsers(result):
     
    users = list()      

    for item in result:
        instance = {"id" : item["id"], "name" : item["name"]}
        users.append(instance)  

    return users

def SplitIds(itemList):       

    newList = itemList.split(",")
    result = list()  

    for item in newList:
        if(item != ""):

            result.append({"id" : int(item)})

    return result


def SplitIdsNoId(itemList):
     
    newList = itemList.split(",")
    result = list()       

    for item in newList:
        if(item != ""):

            result.append(int(item))

    return result

def users (request):    

    if request.session.get("token") == None:            
            return redirect("/login")      

    json_response = GetAPI("/user",request).json()
    user_page = NewPaginator(request,json_response,10,"userPage")
    result = GetAPI("/team",request).json()["team"]
    teams = GetTeams(result)    
   
    return render(request, "webadmin/users.html",{  
             
        "userPage" : user_page,
        "teams" : teams
        
    })

def newUser(request):

    if request.method == "POST":
              
        newUser = NewUser(request.POST)

        if newUser.is_valid():

            name = newUser.cleaned_data["name"]
            email = newUser.cleaned_data["email"]
            selectedTeams = newUser.cleaned_data["teams"]
            teamsFormatted = SplitIds(selectedTeams) 

            session_cookies = request.session.get("token")

            url = api_url + "/user"
            myobj = {"name" : name, 'email': email, "teams" : teamsFormatted}           
            x = requests.post(url, json=myobj, cookies=session_cookies)
            json_response = x.json()

    return HttpResponseRedirect(reverse("users"))

def addOrDeleteTeam(add, userId, teamIds,request):
     
    teamsFormatted = SplitIdsNoId(teamIds)

    myobj = {"user_id" : int(userId), 'teams': teamsFormatted}  
    
    print(myobj)

    session_cookies = request.session.get('token')  
    
    print(session_cookies)

    if add is True:
        x = requests.post(api_url + "/team/user",json=myobj,cookies=session_cookies)
        
    else:
        x = requests.delete(api_url + "/team/user",json=myobj, cookies=session_cookies)

def usersdeleteteam(request):

    if request.method == "POST":

        userId = request.POST["id"]
        teamIds = request.POST["ids"]

        addOrDeleteTeam(False,userId,teamIds,request)

    return HttpResponseRedirect(reverse("users"))

def usersaddteam(request):

    if request.method == "POST":

        userId = request.POST["id"]
        teamIds = request.POST["ids"]

        addOrDeleteTeam(True,userId,teamIds,request)

    return HttpResponseRedirect(reverse("users"))


def deleteMultiple(request,endpoint):  

    if request.method == "POST":      

        session_cookies = request.session.get('token')   

        id = request.POST["id"]
        id = id.split(",")

        ids = list()

        for item in id:
             
             if item != "":
                  
                  ids.append({ "id": int(item) })       
        
        url = api_url + endpoint     
        
        x = requests.delete(url, json=ids,cookies=session_cookies)       

def deleteuser(request):
        
    deleteMultiple(request,"/user/del/")
    return HttpResponseRedirect(reverse("users"))

def edituser(request):
     
    if request.method == "POST":          

        id = request.POST["id"]
        name = request.POST["name"]
        email = request.POST["email"]
        # password = request.POST["password"]
        # code = request.POST["code"]

        session_cookies = request.session.get("token")

        url = api_url + "/user"
        myobj = {"id" : int(id), "name" : name, 'email': email} 
    
        x = requests.put(url, json=myobj, cookies=session_cookies)
        json_response = x.json()   

    return HttpResponseRedirect(reverse("users"))   


def rooms (request):

    if request.session.get("token") == None:            
            return redirect("/login")

    if request.method == "POST":

        obj = {"name" : request.POST["name"]}
        PostAPI("/room", obj,request)  

    rooms = GetAPI("/room",request).json()["room"]
    
    roomsPage = NewPaginator(request,rooms,5,"roomsPage")
    

    return render(request, "webadmin/rooms.html",{

        "roomsPage" : roomsPage,        

    })


def deleteroom(request):        

    deleteMultiple(request,"/room/del/many")
    return HttpResponseRedirect(reverse("rooms"))

def editroom(request):     

    if request.method == "POST":          

        id = request.POST["id"]
        name = request.POST["name"]       

        url = api_url + "/room"
        myobj = {"id" : int(id), "name" : name} 

        session_cookies = request.session.get("token")        

        x = requests.put(url, json=myobj,cookies=session_cookies)
        json_response = x.json()   

    return HttpResponseRedirect(reverse("rooms")) 


def teams(request):

    if request.session.get("token") == None:            
            return redirect("/login") 

    users = GetAPI("/user", request).json()
    users = GetUsers(users)

    teams = GetAPI("/team",request).json()["team"]  
    teamsPage = NewPaginator(request,teams,6,"teamsPage")

    teamsPage = usersAmount(teamsPage)    
    

    if request.method == "POST":
         
        name = request.POST["name"]   
        newUsers = request.POST["users"].split(",")  
        
        userObj = list()       
        
        for item in newUsers:

            if(item != ""):
            
                userObj.append({"id" : int(item)})                
        
        obj = {"name" : name, "users" : userObj}            
                
        PostAPI("/team",obj,request).status_code       

        return HttpResponseRedirect(reverse("teams"))    
        

    return render(request, "webadmin/teams.html",{

        "teamsPage" : teamsPage,
        "users": users,

    })

def teamsaddusers(request):

    if request.method == "POST":

        id = request.POST["id"]        
        ids = request.POST["ids"]
        ids = SplitIdsNoId(ids)
        obj = {"team_id" : int(id), "users" : ids}

        session_cookies = request.session.get("token") 

        url = api_url + "/team/add"

        x = requests.post(url,json=obj,cookies=session_cookies)

        print(x.status_code)

    return HttpResponseRedirect(reverse("teams"))  
    

def teamsdeleteusers(request):

    if request.method == "POST":

        session_cookies = request.session.get('token')       

        id = request.POST["id"]        
        ids = request.POST["ids"]             
        ids = SplitIdsNoId(ids)     

        obj = {"team_id" : int(id), "users" : ids}      

        url = api_url + "/team/remove"

        x = requests.delete(url,json=obj,cookies=session_cookies)

        print(x.status_code)

    return HttpResponseRedirect(reverse("teams"))  
    

def deleteteam(request):
     
    deleteMultiple(request,"/team/del")  
    return HttpResponseRedirect(reverse("teams"))   

def editteam(request):   
     
    if request.method == "POST":          

        id = request.POST["id"]
        name = request.POST["name"] 
        url = api_url + "/team"
       
        myobj = {"id" : int(id), "name" : name}          

        session_cookies = request.session.get("token")      
    
        x = requests.put(url, json=myobj,cookies=session_cookies)
        json_response = x.json()   
    
    return HttpResponseRedirect(reverse("teams"))

def permissions(request):

    rooms = GetAPI("/room",request).json()["room"]
    users = GetAPI("/user",request).json()   
    users = GetUsers(users)           
    teams = GetAPI("/team",request).json()["team"]
    permissions = GetAPI("/permission",request).json()["permissions"]    
    permissionsPage = NewPaginator(request,permissions, 10,"permissionsPage")

    if request.method == "POST":

        form = NewPermission(request.POST)        

        if form.is_valid():            
          
            newUser = ReplaceCommas(form.cleaned_data["users"])
            newRoom = ReplaceCommas(form.cleaned_data["rooms"])
            days =  ReplaceCommas(form.cleaned_data["days"])
            newTeam = ReplaceCommas(form.cleaned_data["teams"])
            startDate = form.cleaned_data["startDate"]
            endDate = form.cleaned_data["endDate"]     
            startTime = form.cleaned_data["startTime"] + ":00"
            endTime = form.cleaned_data["endTime"] + ":00"   

            days = ConvertDays(days)

            startDate = str(startDate)
            endDate = str(endDate)
          
            obj = {
                "room_id": newRoom,
                "team_id": newTeam,
                "user_id": newUser,
                "start_date": startDate,
                "end_date": endDate,
                "start_time": startTime,
                "end_time": endTime,
                "weekdays": days
            }            

            x = PostAPI("/permission", obj,request)      

        return HttpResponseRedirect(reverse("permissions"))        

    return render(request, "webadmin/permissions.html",{

        "users" : users,
        "rooms" : rooms,
        "teams": teams,
        "permissionsPage" : permissionsPage

     })


def deletepermission(request):
     
    deleteMultiple(request,"/permission/del")  
    return HttpResponseRedirect(reverse("permissions"))   



def ConvertDays(days):


    if days == None:

        return None

    if len(str(days)) != 1:    
                days = SplitIds(days)

    else:
        days = [{"id" : days}]


    return days


def editpermission(request):

 if request.method == "POST":

        form = NewPermission(request.POST)        

        if form.is_valid():            
          
            newUser = ReplaceCommas(form.cleaned_data["users"])
            newRoom = ReplaceCommas(form.cleaned_data["rooms"])
            days =  ReplaceCommas(form.cleaned_data["days"])
            newTeam = ReplaceCommas(form.cleaned_data["teams"])
            startDate = form.cleaned_data["startDate"]
            endDate = form.cleaned_data["endDate"]     
            startTime = form.cleaned_data["startTime"] + ":00"
            endTime = form.cleaned_data["endTime"] + ":00"   
            id = request.POST["id"]; 

            days = ConvertDays(days)          

            startDate = str(startDate)
            endDate = str(endDate)

            session_cookies = request.session.get("token")
          
            obj = {
                "id" : int(id),
                "room_id": newRoom,
                "team_id": newTeam,
                "user_id": newUser,
                "start_date": startDate,
                "end_date": endDate,
                "start_time": startTime,
                "end_time": endTime,
                "weekdays": days
            }            

            x = requests.put(api_url + "/permission/",json=obj,cookies=session_cookies) 

        return HttpResponseRedirect(reverse("permissions")) 
 

def history(request):

    history = GetAPI("/history",request).json()["history"]
    history_page = NewPaginator(request,history,10,"historyPage")

    return render(request, "webadmin/history.html",{

        "history_page" : history_page

    })


def set_cookie_and_redirect(cook, redirect_url):
    session_cookies = dict(cook)
    response = HttpResponseRedirect(redirect_url)

    for cookie_name, cookie_value in session_cookies.items():
        response.set_cookie(cookie_name, cookie_value, max_age=3600, domain=".seaofkeys.com")

    return response    

def login(request):
    email = ""
    password = ""
    
    message = ""

    if request.method == 'POST':
        email = request.POST['email_test']
        password = request.POST['password']
        # email = "mkronborg7@gmail.com"
        # password = "Test"  
        url = "https://api.seaofkeys.com/auth/login"

        url = api_url + "/auth/login"

        myobj = {'email': email, "password": password}
        x = requests.post(url, json=myobj)

        if x.status_code == 200:
            token = x.json()["token"]
            session_cookies = dict(x.cookies)         
            request.session['token'] = session_cookies

            redirect_url = reverse("index")
            response = set_cookie_and_redirect(x.cookies, redirect_url)
            return response
        else:
            
            message = "Forkert kode/email"
            
            

    return render(request, "webadmin/login.html", {
        "message" : message
   
    })


def logout(request):
    
    session_cookies = request.session['token']
    x = requests.get(api_url + "/auth/logout",cookies=session_cookies)
    request.session['token'] = None    
    
    return HttpResponseRedirect(reverse("login"))

def test_example(request):

    return HttpResponseRedirect(reverse("index"))

# def team(request,id):

#     if request.session.get("token") == None:            
#             return redirect("/login")   

#     users = []
#     team = Team(1,"Køkkendamerne")


#     for x in range(25):

#         users.append(User(x,"Morten","morten@mail.dk",time))

#     teamUsersPage = NewPaginator(request,users,5,"teamUsersPage")

#     return render(request, "webadmin/team.html",{

#         "teamUsersPage" : teamUsersPage,
#         "team" : team,
#         "users" : users,     

#     })




# def user(request,id):

#     if request.session.get("token") == None:            
#             return redirect("/login")   

#     time = datetime.now().strftime("%H:%M %D")
#     currentUser = User(id,"Morten","bindzus@mail.dk",time) 
#     teams = []

#     userHistory = []

#     for x in range(10):   
#         userHistory.append(historyInstance("Kronborg","Mødelokale 1", x, time)) 

#     for x in range(5):
#         teams.append(Team(x,"Kantinedamerne"))

#     #Pagination
#     team_page = NewPaginator(request,teams,3,"teamPage")
#     history_page = NewPaginator(request,userHistory,3,"userHistory")

#     return render(request, "webadmin/user.html",{
#         "user" : currentUser,
#         "teams" : teams,
#         "history": userHistory,
#         "teamPage" : team_page,
#         "historyPage" : history_page
#     })



# def room(request,id):

#     if request.session.get("token") == None:            
#             return redirect("/login")   


#     teams = []
#     history = []
#     time = datetime.now().strftime("%H:%M %D")    
#     room = Room(1,"Mødelokale",time)

#     for x in range(23):
#         teams.append(Team(x,"Kantinedamerne"))      
#         history.append(historyInstance("Bruger","Dør 1",x,time))

#     teamRoomsPage = NewPaginator(request,teams,5,"teamRoomsPage")
#     historyPage = NewPaginator(request,history,5,"historyPage")


#     return render(request, "webadmin/room.html",{

#         "room" : room,
#         "teams" : teams,
#         "teamRoomsPage" : teamRoomsPage,
#         "historyPage" : historyPage
#     })