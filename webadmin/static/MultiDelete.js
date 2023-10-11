document.addEventListener("DOMContentLoaded", function(){

  var deleteMultiple = document.getElementById("deleteMultiple");	
  var deleteIds = document.getElementById("delete-ids");
  var toBeDeleted = [];		

  var alItems = document.getElementById("all-delete-items");
  var allCheckboxes = document.querySelectorAll(".item-checkbox");
  var selectAll = document.getElementById("selectAll");

  selectAll.addEventListener("click", function(item){

    var isChecked = selectAll.checked;
    allCheckboxes.forEach(function (item){

      if(isChecked){
        item.checked = true;								
      }
      else{
        item.checked = false;				
      }	

    })  
  })	

  deleteMultiple.addEventListener("click", function(){

    toBeDeleted = []
    alItems.innerHTML = " er valgt";
    deleteIds.value = "";

    allCheckboxes.forEach(function (item){

      if(item.checked == true){

        toBeDeleted.push(item.dataset.id);

      }
    })

    toBeDeleted.forEach(function (item){

      deleteIds.value += item + ","

    })

    alItems.innerHTML = toBeDeleted.length + alItems.innerHTML;

  })

})


