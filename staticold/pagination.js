
document.addEventListener("DOMContentLoaded", function(){   

    function SetPagination(next,previous,param){

        var previous_button = document.getElementById(previous);
        var next_button = document.getElementById(next);        

        if(previous_button){
            previous_button.onclick = function(){previous_page(param,previous_button)};
        }
        if(next_button){
            next_button.onclick = function(){next_page(param,next_button)};   
        }    

    }  

    function next_page(param,button){   
            
            var url = new URL(window.location.href);
            var search_params = url.searchParams;        
            search_params.set(param, button.dataset.page);
            url.search = search_params.toString();        
            var new_url = url.toString();      
            window.location = new_url;          
    }

    
    function previous_page(param,button){            
     
            
        var url = new URL(window.location.href);
        var search_params = url.searchParams;        
        search_params.set(param, button.dataset.page);
        url.search = search_params.toString();        
        var new_url = url.toString();  
        window.location = new_url;  
}

    SetPagination("team-next","team-previous","teamPage")
    SetPagination("history-next","history-previous","historyPage")
    SetPagination("users-next","users-previous","userPage")
    SetPagination("teams-next","teams-previous","teamPage")
    SetPagination("teams-next","teams-previous","teamsPage")
    SetPagination("user-history-next","user-history-previous","userHistory")
    SetPagination("rooms-next","rooms-previous","roomsPage")
    SetPagination("room-team-next","room-team-previous","teamRoomsPage");
    SetPagination("team-user-next", "team-user-previous","teamUsersPage")

})