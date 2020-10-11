const showrecipe = 'http://127.0.0.1:5000/api?action=showrecipe';
const checkrecipe = 'http://127.0.0.1:5000/api?action=checkrecipe';

const allre = document.getElementById('allre')
const avail = document.getElementById('avail')
const allredetail = document.getElementById('allredetail')
const availdetail = document.getElementById('availdetail')
const back = document.getElementsByClassName('back')[0];
const add = document.getElementsByClassName('add')[0];

back.addEventListener('click', event=>{
    window.location.href = 'http://127.0.0.1:5000/';
});

add.addEventListener('click', event=>{
    window.location.href = 'http://127.0.0.1:5000/addre';
});


function showre(url){
    fetch(url)
    .then((response) => {
    return response.json();
    }).then((jsontext) =>{
        data = jsontext['cookbook']
        console.log(data);
        addnew(data, 1)
    }).catch((err) => {
    console.log('error:', err);
    });
}

function checkre(url){
    fetch(url)
    .then((response) => {
    return response.json();
    }).then((jsontext) =>{
        data = jsontext['options']
        console.log(data);
        addnew(data, 0)
    }).catch((err) => {
    console.log('error:', err);
    });
}

allre.onclick = function () {
    showre(showrecipe);
}

avail.onclick = function () {
    checkre(checkrecipe);
}

function addnew(data,order){
    for(let i = 0; i < data.length; i++){
        var node = document.createElement("LI"); 
        node.setAttribute("class", "item");
        node.innerHTML = "<button class='re_name' onclick='location.href='"+data[i][9]+" '>"+data[i][0]+"</button>"
        console.log(data[i][9])
        document.getElementsByClassName("itemlist")[order].appendChild(node);
        for(let j = 1; j < data[i].length-1; j+=2){
            var subnode = document.createElement("LI"); 
            subnode.setAttribute("class", "material");  
            subnode.innerHTML += "<div class='material_name'>"+data[i][j]+": "+data[i][j+1]+"</div>"
            node.appendChild(subnode);  
        }
    }
}