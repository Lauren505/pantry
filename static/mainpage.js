const mainpage = 'http://127.0.0.1:5000/api?action=update';
const invpart = 'http://127.0.0.1:5000/api?action=invpart';

const temp = document.getElementById('temp')
const humi = document.getElementById('humi')
const warn = document.getElementById('warn')
const refr = document.getElementById('refr')



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
    console.log('error:', err);
    });
}

setInterval(refresh(mainpage), 1000);
refr.onclick = function () {
    refresh(mainpage);
}

