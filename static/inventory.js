const invall = 'http://127.0.0.1:5000/api?action=invall';
const sall = document.getElementById('sall')
const egg = document.getElementById('egg')
const item_list = [];
const exp_item_list = [];
const exp_date_input = document.getElementById("expireddays");
const today = new Date();

exp_date_input.addEventListener('keyup', event => {
    if(event.keyCode === 13 && event.target.value !== ''){
        const range = event.target.value;
        console.log("range: " + range);
        ShowItemsExipredInDays(today, range);
    }
})

function inve(url){
    fetch(url)
    .then((response) => {
    return response.json();
    }).then((jsontext) =>{
        console.log(jsontext);
        database = jsontext['inv'];
        dataHandling(database);
        for(let i = 0; i < database.length; i++){
            const new_item = additem(database[i][0], database[i][1], database[i][2], i);
            const item_exp = database[i][2].split('-');
            if(ConvertStringToDate(item_exp).getTime() < today.getTime()){
                exp_item_list.push(new_item);
                document.getElementById("exp_list_root").appendChild(new_item);
            }
            else{
                item_list.push(new_item);
                document.getElementById("list_root").appendChild(new_item);
            }
            
        }
        
    }).catch((err) => {
    console.log('error:', err);
    });
}

window.onload = function() {
    inve(invall);
}

sall.onclick = function () {
    ShowAllItems();
}

function dataHandling(data){
    console.log(data);
    console.log(data.length);
}

function additem(name, weight, date, id){
    const li_ele = document.createElement("LI");
    const ele_name = document.createElement("DIV");
    const ele_weight = document.createElement("DIV");
    const ele_date = document.createElement("DIV");
    const name_p = document.createElement("P");
    const weight_p = document.createElement("P");
    const date_p = document.createElement("P");
    li_ele.setAttribute("class", "itemdetail");
    li_ele.setAttribute("id", id)
    ele_name.setAttribute("class", "itemdetail-name");
    ele_weight.setAttribute("class", "itemdetail-weight");
    ele_date.setAttribute("class", "itemdetail-date");
    name_p.textContent = name;
    weight_p.textContent = weight;
    date_p.textContent = date;
    ele_name.appendChild(name_p);
    ele_weight.appendChild(weight_p);
    ele_date.appendChild(date_p);
    li_ele.appendChild(ele_name);
    li_ele.appendChild(ele_weight);
    li_ele.appendChild(ele_date);
    return li_ele;
}

function ShowAllItems(){
    console.log("show all items");
    for(let i = 0; i < item_list.length; i++){
        item_list[i].style["display"] = "flex";
    }
}

function ShowItemsExipredInDays(today, range){
    console.log("show expiring items");
    range_date = new Date(today);
    range_date.setDate(range_date.getDate() + parseInt(range, 10));
    for(let i = 0; i < item_list.length; i++){
        const item_index = parseInt(item_list[i].id, 10);
        const exp_arr = database[item_index][2].split('-');
        exp_date = ConvertStringToDate(exp_arr);
        //console.log(exp_date);
        if(exp_date.getTime() < range_date.getTime()){
            //console.log("the item with index" + i + "is in the range");
            item_list[i].style["display"] = "flex";
        }
        else{
            item_list[i].style["display"] = "none";
        }
    }
}

function ConvertStringToDate(arr){
    const year = parseInt(arr[0], 10);
    const month = parseInt(arr[1], 10) - 1;
    const day = parseInt(arr[2], 10);
    const date = new Date(year, month, day);
    return date;
}

