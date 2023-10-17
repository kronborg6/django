document.addEventListener("DOMContentLoaded", function(){  
    
class MultiSelect {
    constructor(elementName) 
    {
        this.elementName = elementName;    
    } 

    Init()
    {        
        var resultElement = document.getElementById(this.elementName);  
        var itemInputs = [];             
        var elementName = this.elementName;

        document.querySelectorAll(".multiSelectItem").forEach(function (item){              
                        
            if(item.dataset.multiselect == elementName)            
            {
                itemInputs.push(item); 
            }
        })       

        itemInputs.forEach(function (item){	
	
            item.addEventListener("change", function(){      
                
                resultElement.value = "";
    
                itemInputs.forEach(function (i){    
    
                    if(i.checked == true){
                        
                        resultElement.value += i.value + ",";
                    }
    
                })  
                
            })
        
        })
    }

}

    function InitSelectors(items){      

        items.forEach(function (item){            

            var multiSelect = new MultiSelect(item.dataset.multiselect);           
            multiSelect.Init();  

        })
    }
    
    InitSelectors(document.querySelectorAll(".multiSelectItem"));

})