
    function extend_second_list(arrow) {
        let i = arrow.id[6];
        let list = $("#second-list-"+i);
        let to_hide = list.hasClass("close");

        if(to_hide){
            list.slideDown(400);
            list.removeClass("close");
            list.parent().css("backgroundColor", "#d2dff8");

        }else{
            list.slideUp(400);
            list.addClass("close");
            list.parent().css("backgroundColor", "");

        }
        (arrow.style.transform === "" || arrow.style.transform === "rotateX(0deg)") ?
        arrow.style.transform ="rotateX(180deg)": arrow.style.transform ="rotateX(0deg)";
    }

    let arrows = document.getElementsByClassName("arrow");
    for (let i = 0; i < arrows.length; i++) {
        arrows[i].addEventListener('click', function (){extend_second_list(arrows[i]);} , false);
    }
