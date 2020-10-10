const invall = 'http://127.0.0.1:5000/api?action=invall';
const invpar = 'http://127.0.0.1:5000/api?action=invpar';
const sall = document.getElementById('sall')
const egg = document.getElementById('egg')
const done = document.getElementById('done')

function inve(url){
    fetch(url)
    .then((response) => {
    return response.json();
    }).then((jsontext) =>{
        console.log(jsontext);
        
    }).catch((err) => {
    console.log('error:', err);
    });
}

sall.onclick = function () {
    inve(invall);
}

function invp(url){
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

done.onclick = function () {
    invp(invpar);
}
