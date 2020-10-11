const back = document.getElementsByClassName('back')[0];
const com = 'http://127.0.0.1:5000/api?action=common';
const itemn = document.getElementById('itemname')

back.addEventListener('click', event=>{
    window.location.href = 'http://127.0.0.1:5000/';
});

function common(url){
    fetch(url)
    .then((response) => {
    return response.json();
    }).then((jsontext) =>{
        data = jsontext['common']
        console.log(data);
        for(let i = 0; i < data.length; i++){
            addnew(i, data[i])
        }
    }).catch((err) => {
        console.log('refresh error:', err);
    });
}

function addnew(i, name){
    var node = document.createElement("LI"); 
    node.setAttribute("class", "item");        
    node.innerHTML = "<input type='button' id='opt"+i+"' class='itemdetail' value='"+name+"' onclick='addtoinput(this)'>"                
    document.getElementsByClassName("itemlist")[0].appendChild(node);
}

window.onload = function() {
    common(com);
}

function addtoinput(myObj){
    id = myObj.id
    val = myObj.value
    console.log("val: ", val)
    itemn.value = val
    
}
