
document.addEventListener("DOMContentLoaded", function(){

    const previous_button = document.getElementById("previous");
    const next_button = document.getElementById("next");

    const history_previous = document.getElementById("history-previous");
    const history_next = document.getElementById("history-next");    

    if(previous_button){
        previous_button.onclick = function(){previous_page("userPage",previous_button)};
    }
    if(next_button){
        next_button.onclick = function(){next_page("userPage",next_button)}; 
    }
    
    if(history_previous){
        history_previous.onclick = function(){previous_page("historyPage",history_previous)};
    }
    if(history_next){
        history_next.onclick = function(){next_page("historyPage",history_next)};   
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

})