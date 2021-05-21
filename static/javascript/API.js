//scrolling updates
let date = new Date();
let hour = (date.getHours().toString().length < 2 ? '0'+date.getHours() : date.getHours()); //concat zero if single-digit
let min = (date.getMinutes().toString().length < 2 ? '0'+date.getMinutes() : date.getMinutes()); //concat zero if single-digit
document.getElementById('date-input').valueAsDate = date;
document.getElementById('time-input').value = hour+":"+min;

//drop area
function drop(ev){
    ev.preventDefault();
    console.log("file dropped");
    let dt = ev.dataTransfer;
    let files = dt.files;
    console.log(files);

}
function allowDrop(ev) {
    ev.preventDefault();
}

/*------------ HELP FUNCTIONS --------------*/
const getFormJSON = (form) => {
    const data = new FormData(form);
    return Array.from(data.keys()).reduce((result, key) => {
        result[key] = data.get(key);
        return result;
    }, {});
};

const sendToServer = (url, method, data)=>{
    fetch(url, {
        // Specify the method
        method: method,
        // A JSON payload
        body: JSON.stringify(data),
        headers: {'Content-type': 'application/json; charset=UTF-8'}
    }).then(function (response) {
        console.log(response);
        return response.json();
    }).then(function (text) {
        console.log(text);
        alert(`${method} response: ${JSON.stringify(text,undefined,4)}`);
        location.reload();
    });
};


/*------------ NEWS FUNCTIONS --------------*/
//add news
function  addNewsSubmit(ev) {
    ev.preventDefault();
    let add_news_form = document.getElementById("add-news-form");
    let data = getFormJSON(add_news_form);
    let dateObj = new Date(data["date-input"]);
    const month = dateObj.getUTCMonth() + 1; //months from 1-12
    const day = dateObj.getUTCDate();
    const year = dateObj.getUTCFullYear();
    date = day + '/' + month + '/' + year + " " + data["time-input"];

    data = {"message": data["flashNews-input"], "date_time": date};
    // console.log(date)
    sendToServer('/flashNews', 'POST', data);
}

//delete news
function deleteNewsSubmit(ev){
    ev.preventDefault();
    let delete_news_form = document.getElementById("delete-news-form");
    let data = getFormJSON(delete_news_form);

    let key;
    for(key in data){
        let json = JSON.parse(data[key]);
        let datetime = json["date"].split(" ")[1] + " " + json["time"]; //fix date format to "dd/mm/yyyy hh:mm" , get just date without the day text a
        let json_to_delete = {"message": json["news"], "date_time": datetime };
        console.log(json_to_delete);
        sendToServer('/flashNews', 'DELETE', json_to_delete);
    }
}

/*------------ DATATABLE FUNCTIONS --------------*/
//add datatable
function addDatatableSubmit(ev){
    ev.preventDefault();
    let add_datatable_form = document.getElementById("add-dataTable-form");
    let data = getFormJSON(add_datatable_form);
    console.log(data);
    sendToServer('/DataTable', 'POST', data);
}

//delete source
function deleteDatatableSubmit(ev){
    ev.preventDefault();
    let delete_source_form = document.getElementById("delete-dataTable-form");
    let data = getFormJSON(delete_source_form);
    sendToServer('/DataTable', 'DELETE', data);
}

/*------------ SOURCES FUNCTIONS --------------*/
//add source
function addSourceSubmit(ev){
    ev.preventDefault();
    let add_source_form = document.getElementById("add-source-form");
    let data = getFormJSON(add_source_form);
    sendToServer('/source', 'POST', data);
}

//delete source
function deleteSourceSubmit(ev){
    ev.preventDefault();
    let delete_source_form = document.getElementById("delete-source-form");
    let data = getFormJSON(delete_source_form);
    sendToServer('/source', 'DELETE', data);
}

/*------------ POSTS FUNCTIONS --------------*/
//add posts
function addPostSubmit(ev){
    ev.preventDefault();
    let add_post_form = document.getElementById("add-post-form");
    let data = getFormJSON(add_post_form);
    console.log(data);
    sendToServer('/post','POST', data)
}