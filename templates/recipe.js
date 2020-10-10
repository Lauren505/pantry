const showrecipe = 'http://127.0.0.1:5000/api?action=showrecipe';
const checkrecipe = 'http://127.0.0.1:5000/api?action=checkrecipe';

const allre = document.getElementById('allre')
const avail = document.getElementById('avail')
const allredetail = document.getElementById('allredetail')
const availdetail = document.getElementById('availdetail')


function showre(url){
    fetch(url)
    .then((response) => {
    return response.json();
    }).then((jsontext) =>{
        console.log(jsontext);
        allredetail.innerHTML = jsontext;
    }).catch((err) => {
    console.log('error:', err);
    });
}

function checkre(url){
    fetch(url)
    .then((response) => {
    return response.json();
    }).then((jsontext) =>{
        console.log(jsontext);
        availdetail.innerHTML = jsontext['inv'];
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

