document.addEventListener("DOMContentLoaded", function(){

  var url = "https://api.seaofkeys.com"

  var currentId = document.getElementById("add-id");
  var currentIds = document.getElementById("add-ids");

  var info = document.getElementById("info");

  function clear(){

    var warnings = document.querySelectorAll(".warning");
    warnings.forEach(function (item){
      item.remove();
    })  
    var parent = document.getElementById("addOptions");
    parent.innerHTML = "";  
  }
  
  function getvals(id, endpoint){
    return fetch(url +  endpoint + id ,
    {
      method: "GET",
      credentials: "include",
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


      if(info.dataset.title == "teams"){
        response = response["users"]
      }
      else if(info.dataset.title == "users")
      {
        response = response["teams"]
      }   


      var parent = document.getElementById("addOptions");     
      

      if(response.length > 0){        
  
        var multiTemplateInput = document.getElementById("multiTemplateInputEdit");
        var multiTemplateLabel = document.getElementById("multiTemplateLabelEdit");
    
    
        response.forEach(function (item){    
    
          const inputClone = multiTemplateInput.cloneNode(true);  
          const labelClone = multiTemplateLabel.cloneNode(true);     
    
          const newDiv = document.createElement("div");
          newDiv.classList.add("d-flex");
    
          parent.appendChild(newDiv);      
  
          inputClone.value = item.id;
          labelClone.innerHTML = item.name;
    
          labelClone.classList.add("m-0");
          labelClone.classList.add("m-1");
    
          inputClone.style.display = "block";
          labelClone.style.display = "block";
    
          inputClone.classList.remove("template");
          labelClone.classList.remove("template");
  
          inputClone.classList.add("addInputFields");
        
          newDiv.appendChild(inputClone);
          newDiv.appendChild(labelClone);
  
          inputClone.addEventListener("change", function(){
  
            currentIds.value = "";      
  
            allEditInputs = document.querySelectorAll(".addInputFields");
            allEditInputs.forEach(function (item){     
              
  
              if(item.checked == true){             
  
                currentIds.value += item.value + ",";
              }
  
            })     
  
          });  
        })  

      }
      else
      {

        const p = document.createElement("p");
        p.innerHTML = "Ikke flere " + info.dataset.items;
        p.classList.add("warning")
        parent.appendChild(p);       

      }      
    }  

    addNoneButtons = document.querySelectorAll(".addNone");

    addNoneButtons.forEach(function (item){

      item.addEventListener("click", function(){

        clear()
        
        currentId.value = item.dataset.id;
        getvals(item.dataset.id,info.dataset.addendpoint).then(response => setResponse(response));
        
      })

    })

})

