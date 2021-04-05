let tags_to_show = [];

/*This function removing element from list*/
function removeElement(ls,el) {
    const index = ls.indexOf(el);
    if (index > -1) {
      ls.splice(index, 1);
    }
}
/*This function get tag name and update tags_to_show list that hold all tags for filtering. Then call Filter()*/
function FilterByTag(chosenTag){
    //remove filter "all" if another choose
    if(chosenTag !=="הצג הכל" && tags_to_show.includes("הצג הכל")){
        removeElement(tags_to_show,"הצג הכל");
        document.getElementById("btn_" + "הצג הכל").classList.toggle("clicked");
    }

    //delete chosenTag from tags_to_show list if the button unchecked
    if(tags_to_show.includes(chosenTag)) {
        removeElement(tags_to_show,chosenTag);
    }

    //add chosenTag to tags_to_show list
    else {
        tags_to_show.push(chosenTag);
        console.log(chosenTag);
    }

    //styling pushed button and filter updates by tags_to_show
    document.getElementById("btn_" + chosenTag).classList.toggle("clicked");
    Filter();
}

/*This function move over each update-container, check if at least one of it's tags exist in the filters list:
* if exist - show the update, else- hide it*/
function Filter(){

    let tags_div_ls = document.querySelectorAll("#tags_container");

    // loop for pass each update-container
    for (let i = 0; i < tags_div_ls.length; i++){
        let num_of_tags = tags_div_ls[i].childElementCount;
        let to_hide = true;

        // loop for pass each tag of current update
        for (let j = 1; j <= num_of_tags; j++) {
            let tag = tags_div_ls[i].querySelector(":nth-child(" + j + ")").innerHTML;
            if (tags_to_show.includes(tag) || tags_to_show.includes("הצג הכל") || tags_to_show.length === 0) {
                to_hide = false;
            }
        }

        let mail_to_hide = $("#mail_container_"+i);
        to_hide? mail_to_hide.slideUp(400) : mail_to_hide.slideDown(400);

       //  let mail_to_hide = document.getElementById("mail_container_" + i);
       // to_hide ? mail_to_hide.style.display = "none" :mail_to_hide.style.display = "";
    }
}