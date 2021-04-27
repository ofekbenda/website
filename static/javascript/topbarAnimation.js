// navigate dropdown list animation - exit and show\hide navigate list
let dropdown_nav = document.getElementById("dropdown-nav");
// let screen = document.getElementById("dropdown-menu-container");

dropdown_nav.addEventListener("click", navClick);
// screen.addEventListener("click", navClick);

function navClick() {
    if(dropdown_nav.classList.contains("close")){
        dropdown_nav.classList.remove("close");
        document.getElementById("row-1").style.transform = "rotate(-45deg)";
        document.getElementById("row-2").style.transform = "rotateY(90deg)";
        document.getElementById("row-3").style.transform = "rotate(45deg)";
        document.getElementById("dropdown-menu-container").style.visibility="visible";
        document.getElementById("dropdown-menu-container").style.opacity="1";

    } else{
        dropdown_nav.classList.add("close");
        document.getElementById("row-1").style.transform = "";
        document.getElementById("row-2").style.transform = "";
        document.getElementById("row-3").style.transform = "";
        document.getElementById("dropdown-menu-container").style.visibility="hidden";
        document.getElementById("dropdown-menu-container").style.opacity="0";

    }
}

// When the user scrolls down 600 from the top of the document, change topbar style
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    let topbar_element = document.getElementById("topbar");
    if ((document.body.scrollTop > 600 || document.documentElement.scrollTop > 600)) {
        document.getElementById("topbar").style.background = "linear-gradient(to bottom, #f0f0f0 0%, rgba(255, 255, 255, 0.9) 80%, white 100%)";

    } else {
        document.getElementById("topbar").style.background = "linear-gradient(to bottom, #f0f0f0 0%, rgba(255, 255, 255, 0.5) 80%, rgba(255, 255, 255, 0) 100%)";
    }
}
