document.addEventListener("DOMContentLoaded", function(){

class Paginator {
    constructor(button, param) 
    {
        this.button = button;
        this.param = param;
        
    }  

    SetPage (page){

        var url = new URL(window.location.href);
        var search_params = url.searchParams;        
        search_params.set(this.param, page);
        url.search = search_params.toString();        
        var new_url = url.toString();      
        window.location = new_url;        
    }    

    SetButtons (){        

        if(this.button){
            this.button.onclick = () => this.SetPage(this.button.dataset.page);
        }
    }

  }

  function Paginate(paginators){

    paginators.forEach(function (item){        

            var paginator = new Paginator(item, item.dataset.param)
            paginator.SetButtons();        

        })
    }

    var paginators = document.querySelectorAll(".pagination-button");
    Paginate(paginators);   

})