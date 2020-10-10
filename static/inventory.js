const invall = 'http://127.0.0.1:5000/api?action=invall';
const sall = document.getElementById('sall')
const egg = document.getElementById('egg')

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
