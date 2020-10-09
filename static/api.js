const mainpage = 'http://127.0.0.1:5000/api?action=update';
const invall = 'http://127.0.0.1:5000/api?action=invall';
const invpart = 'http://127.0.0.1:5000/api?action=invpart';
const recipe = 'http://127.0.0.1:5000/api?action=recipe';
const temp = document.getElementById('temp')
const humi = document.getElementById('humi')
const warn = document.getElementById('warn')
const refr = document.getElementById('refr')
const sall = document.getElementById('sall')
const part = document.getElementById('part')
const reci = document.getElementById('reci')


function postback(url){
    fetch(url)
    .then((response) => {
    return response.json();
    }).then((jsontext) =>{
        console.log(jsontext);
        return jsontext;
    }).catch((err) => {
    console.log('error:', err);
    });
}

setInterval(postback(mainpage), 1000);
refr.onclick = function () {
    data = postback(mainpage);
    temp.innerHTML = data['temp']
    humi.innerHTML = data['humid']
    warn.innerHTML = data['warning']
}
sall.onclick = function () {
    console.log("hi")
    data = postback(invall);
}
part.onclick = function () {
    data = postback(invpart);
}
reci.onclick = function () {
    data = postback(recipe);
}