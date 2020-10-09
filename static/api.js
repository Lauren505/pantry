let url = 'http://127.0.0.1:5000/api?action=update';

fetch(url)
.then((response) => {
console.log(response);
return response.json();
}).catch((err) => {
console.log('錯誤:', err);
});