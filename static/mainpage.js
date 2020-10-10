const mainpage = 'http://127.0.0.1:5000/api?action=refresh';
const updweight = 'http://127.0.0.1:5000/api?action=update';

const temp = document.getElementById('temp')
const humi = document.getElementById('humi')
const warn = document.getElementById('warn')
const refr = document.getElementById('refr')
const updaw = document.getElementById('updaw')
const inventory = document.getElementsByClassName('box')[0];
const recipe = document.getElementsByClassName('box')[1];
const add = document.getElementsByClassName('box')[2];

inventory.addEventListener('click', event=>{
    window.location.href = 'http://127.0.0.1:5000/inventory';
});

recipe.addEventListener('click', event=>{
    window.location.href = 'http://127.0.0.1:5000/recipe';
});

add.addEventListener('click', event=>{
    window.location.href = 'http://127.0.0.1:5000/add';
});

function refresh(url){
    fetch(url)
    .then((response) => {
    return response.json();
    }).then((jsontext) =>{
        console.log(jsontext);
        temp.innerHTML = jsontext['temp'];
        humi.innerHTML = jsontext['humid'];
        warn.innerHTML = jsontext['warning'];
        test.innerHTML = jsontext['inv'];
    }).catch((err) => {
        console.log('refresh error:', err);
    });
}

setInterval(refresh(mainpage), 1000);
refr.onclick = function () {
    refresh(mainpage);
}

function update(url){
    fetch(url)
    .then((response) => {
    return response.json();
    }).then((jsontext) =>{
        console.log(jsontext);
        temp.innerHTML = jsontext['temp'];
    }).catch((err) => {
        console.log('refresh error:', err);
    });
}

setInterval(refresh(mainpage), 1000);
refr.onclick = function () {
    refresh(mainpage);
}