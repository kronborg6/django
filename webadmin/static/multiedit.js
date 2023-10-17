document.addEventListener("DOMContentLoaded", function(){

  var url = "https://api.seaofkeys.com"

  var editButton = document.querySelectorAll(".edit");
  var editusersInput = document.getElementById("editusers");

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
      
      var users = response["team"]["users"]
      
      var parent = document.getElementById("mySelectOptionsEdit");
      var multiTemplateInput = document.getElementById("multiTemplateInput");
      var multiTemplateLabel = document.getElementById("multiTemplateLabel");

      editusersInput.value = "";  
      parent.innerHTML = "";  

      var index = 1;
  
      users.forEach(function (item){

        if(users.length == index){

          editusersInput.value += item.id;  
        }
        else{
          editusersInput.value += item.id + ",";    
        }
  
        const inputClone = multiTemplateInput.cloneNode(true);   


        //Sets input field value if checked or not
        inputClone.addEventListener("change", function(){

          editusersInput.value = "";               
          allEditInputs = document.querySelectorAll(".multiEditInput");

          allEditInputs.forEach(function (item){

            if(item.checked == true){

              editusersInput.value += item.value + ",";
            }

          })     

        });
        
        const labelClone = multiTemplateLabel.cloneNode(true);   
        
        inputClone.checked = true;
  
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

        inputClone.classList.add("multiEditInput");
      
        newDiv.appendChild(inputClone);
        newDiv.appendChild(labelClone);

        index++;       
  
      })
  
    }

    editButton.forEach(function (item){

      item.addEventListener("click", function (){      
  
        getvals(item.dataset.id,"/team/").then(response => setResponse(response));           
  
      })
  
    })	  
})


