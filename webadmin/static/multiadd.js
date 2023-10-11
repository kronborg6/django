document.addEventListener("DOMContentLoaded", function(){

  var url = "https://api.seaofkeys.com"
  var addItemTop = document.getElementById("addItem");
  var editusersInput = document.getElementById("usersToBeAdded");

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
      
      var parent = document.getElementById("mySelectOptions");
      var multiTemplateInput = document.getElementById("multiTemplateInputEdit");
      var multiTemplateLabel = document.getElementById("multiTemplateLabelEdit");
  
      parent.innerHTML = "";   
  
      response.forEach(function (item){
  
        const inputClone = multiTemplateInput.cloneNode(true);       
        const labelClone = multiTemplateLabel.cloneNode(true);     
  
        const newDiv = document.createElement("div");
        newDiv.classList.add("d-flex");
  
        parent.appendChild(newDiv);

        inputClone.addEventListener("change", function(){

          editusersInput.value = "";               
          allEditInputs = document.querySelectorAll(".multiEditInput");

          allEditInputs.forEach(function (item){

            if(item.checked == true){

              editusersInput.value += item.value + ",";
            }

          })     

        });

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
  
      })  
    }
  
    addItemTop.addEventListener("click", function(){
      
      getvals("","/user").then(response => setResponse(response));   
  
    }) 
  
})


