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
            addnew()
        }
    }).catch((err) => {
        console.log('refresh error:', err);
    });
}

function addnew(i, name){
    var node = document.createElement("LI"); 
    node.setAttribute("class", "item");        
    node.innerHTML = "<li class='item'><input type='button' id='opt"+i+"' class='itemdetail' value='"+name+"'></li>"                
    document.getElementsByClassName("itemlist")[0].appendChild(node);
}

setInterval(common(com), 5000);
itemn.onclick = function () {
    common(com);
}
