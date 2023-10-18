document.addEventListener("DOMContentLoaded", function (){ 

//Sets id of what to edit
var editUsers = document.querySelectorAll(".edit")
var deleteUsers = document.querySelectorAll(".delete")

var editId = document.getElementById("edit-id");
var deleteId = document.getElementById("delete-id");

function SetEditText(userId){

  emails = document.querySelectorAll(".user-email").forEach(function (item){

    if(item.dataset.id == userId){
      document.getElementById("edit-mail").value = item.innerHTML
    }

  })

  names = document.querySelectorAll(".user-name").forEach(function (item){
  

    if(item.dataset.id == userId){
      document.getElementById("edit-name").value = item.innerHTML
    }

  })

}

editUsers.forEach(function (item){

  item.addEventListener("click", function(){

    editId.value = item.dataset.id;
    SetEditText(item.dataset.id);

  })
})


deleteUsers.forEach(function (item){

  item.addEventListener("click", function (){

    deleteId.value = item.dataset.id;

  })
})	
})
