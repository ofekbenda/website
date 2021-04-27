    function ScrollToTop(){
        window.scrollTo({top: 0, behavior: "smooth"});
    }

    //scrolling top after refresh
    window.onload=function () { ScrollToTop() };

    //scrolling top when button clicked
    let up_btn = document.getElementById("button-top");
    up_btn.onclick = function(){ ScrollToTop() };

    //scrolling to selected source
    let selected = document.getElementById("input-sources-list");
    function scroll_to_selected(){
        let selected_value =selected.value;
        let selected_element = document.getElementById(selected_value);
        let headerOffset = 100;
        let elementPosition = selected_element.getBoundingClientRect().top;
        let offsetPosition = elementPosition - headerOffset;

        window.scrollTo({
             top: offsetPosition,
             behavior: "smooth"
        });
    }
    //activate scrolling when selected changed or when enter clicked
    selected.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            scroll_to_selected();
        }
    });
    selected.onchange = function (){scroll_to_selected()};