document.addEventListener("DOMContentLoaded", function(){

  var url = "https://api.seaofkeys.com"

  var editButton = document.querySelectorAll(".edit");
  var permissionToBeEdited = document.getElementById("permissionToBeEdited");
  var EditItems = [];

  var roomsInput = document.querySelectorAll(".roomsToBeEdited");
  var teamsInput = document.querySelectorAll(".teamsToBeEdited");  
  var usersInput = document.querySelectorAll(".usersToBeEdited");

  var startDateEdit = document.getElementById("startDateEdit");
  var endDateEdit = document.getElementById("endDateEdit");

  var startTimeEdit = document.getElementById("startTimeEdit");
  var endTimeEdit = document.getElementById("endTimeEdit")

  var mondayEdit = document.getElementById("mondayEdit");
  var tuesdayEdit = document.getElementById("tuesdayEdit");
  var wednesdayEdit = document.getElementById("wednesdayEdit");
  var thursdayEdit = document.getElementById("thursdayEdit");
  var fridayEdit = document.getElementById("fridayEdit");
  var saturdayEdit = document.getElementById("saturdayEdit");
  var sundayEdit = document.getElementById("sundayEdit");


  
  var usersTotal = document.getElementById("usersToBeEdited");
  var roomsTotal = document.getElementById("roomsToBeEdited");
  var daysTotal = document.getElementById("daysOfTheWeekEdited");
  var teamsTotal = document.getElementById("teamsToBeEdited");


  EditItems.push(mondayEdit,tuesdayEdit,wednesdayEdit,thursdayEdit,fridayEdit,saturdayEdit,sundayEdit)  
  

  function getvals(id, endpoint){
    return fetch(url +  endpoint + id ,
    {
      method: "GET",
      headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      },
    })
    .then((response) => response.json())
    .then((responseData) => {		  
      return responseData;
    })
    .catch(error => console.warn(error));
    }  
  
    function setResponse(response){      
      
      var roomId = response["permission"]["room_id"]
      var teamId = response["permission"]["team_id"]
      var userId = response["permission"]["user_id"]      

      var startDate = response["permission"]["start_date"]
      var endDate = response["permission"]["end_date"]

      var startTime = response["permission"]["start_time"];
      var endTime = response["permission"]["end_time"];

      var weekdays = response["permission"]["weekdays"]

      roomsInput.forEach(function (item){

        if(item.value == roomId)
        {
          item.checked = true;
          roomsTotal.value = roomId;
        }  
        else{
          item.checked = false;
        }
      })

      teamsInput.forEach(function (item){

        if(item.value == teamId)
        {
            item.checked = true;
            teamsTotal.value = teamId;
        }
        else{
          item.checked = false;
        }
      })


      usersInput.forEach(function (item){

        if(item.value == userId){
          item.checked = true;
          usersTotal.value = userId;
        }
        else{
          item.checked = false;
        }

      })


      startDateEdit.value = startDate;
      endDateEdit.value = endDate;

      startTimeEdit.value = startTime;
      endTimeEdit.value = endTime;

      weekdays.forEach(function (weekday) {

        switch (weekday.name) {
          case "Monday":
            mondayEdit.checked = true;
            
            daysTotal.value += weekday.id + ","
            break;
          case "Tuesday":       
            tuesdayEdit.checked = true;
            
            daysTotal.value += weekday.id + ","
            break;
          case "Wednesday":
            wednesdayEdit.checked = true;
            
            daysTotal.value += weekday.id + ","
            break;
          case "Thursday":
            thursdayEdit.checked = true;
            
            daysTotal.value += weekday.id + ","
            break;
          case "Friday":
            fridayEdit.checked = true;
            
            daysTotal.value += weekday.id + ","
            break;
          case "Saturday":
            saturdayEdit.checked = true;
            
            daysTotal.value += weekday.id + ","
            break;
          case "Sunday":
            sundayEdit.checked = true;
           
            daysTotal.value += weekday.id + ","
            break;
        }
      })     
      
   
    }

    editButton.forEach(function (item){

      item.addEventListener("click", function (){   

        permissionToBeEdited.value = item.dataset.id

        clear();
  
        getvals(item.dataset.id,"/permission/").then(response => setResponse(response));           
  
      })
  
    })

    function clear(){

      usersTotal.value = ".";
      roomsTotal.value = ".";
      daysTotal.value = "";
      teamsTotal.value = ".";    

      roomsInput.forEach(function (item){

        item.checked = false;
      })
      usersInput.forEach(function (item){

        item.checked = false;
      }
      )
      teamsInput.forEach(function (item){

        item.checked = false;
      })

      EditItems.forEach(function (item){

        item.checked = false;
      })

    }
})


