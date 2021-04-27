
    let selected = document.getElementById("input-databasesInfo-list");
    let iframe_info = document.createElement('iframe');
    let iframe_dash = document.createElement('iframe');
    iframe_info.setAttribute("id", "iframe-info");
    iframe_dash.setAttribute("id", "iframe-dash");

    //load information and dashboard then selected in droplist
    function get_html() {

        let info_div = document.getElementById("info-frame-container");
        let dash_div = document.getElementById("dash-frame-container");

        //remove default info and dash
        $("#default-info-container").fadeOut();
        $("#default-dash-container").fadeOut();

        //add load animation
        info_div.style.backgroundImage="url('../images/loader.gif')";
        dash_div.style.backgroundImage="url('../images/loader.gif')";

        let ind = document.getElementsByClassName(selected.value)[0].id; //get ind of pages to load

        //parsing info and dashboards array
        let url_arr = {{ data[1]|safe|replace(" ",",") }}

        let dash_arr = {{ data[2]|safe|replace(" ",",") }}

        //load url to iframes
        iframe_info.src = url_arr[ind]+"#firstHeading";
        iframe_dash.src = dash_arr[ind];

        //link the iframe element to his container
        info_div.appendChild(iframe_info);
        dash_div.appendChild(iframe_dash);
    }
    selected.onchange = function (){get_html()};

    //show info if "info-title" clicked
    let info = document.getElementById("info-title-container");
    info.onclick= function (){
        $("#info-frame-container").slideToggle();
        //change arrow direction
        let info_arrow = document.getElementById("info-arrow");
        (info_arrow.style.transform === "" || info_arrow.style.transform === "rotateX(0deg)") ?
        info_arrow.style.transform ="rotateX(180deg)": info_arrow.style.transform ="rotateX(0deg)";

    };

    //show dashboard if "dash-title" clicked
    let dash = document.getElementById("dash-title-container");
    dash.onclick= function (){
        $("#dash-frame-container").slideToggle();
        //change arrow direction
        let dash_arrow = document.getElementById("dash-arrow");
        (dash_arrow.style.transform === "" || dash_arrow.style.transform === "rotateX(0deg)") ?
        dash_arrow.style.transform ="rotateX(180deg)": dash_arrow.style.transform ="rotateX(0deg)";
    };