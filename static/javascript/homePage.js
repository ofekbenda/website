/*The function adds the animation slideUp for the scrolling area according to the current window size.
In addition - calculate and update duration animation proportionately to num of updates and window size.
 */
let fit_scroll_properties = function() {
        let scrolling_content = document.getElementById("all-updates-container");
        let scrolling_area = document.getElementById("scrolling-area");
        let height_scrolling_content = scrolling_content.offsetHeight;
        let height_scrolling_area = scrolling_area.offsetHeight;

    //override old Style with new one with updates properties
        let len = scrolling_content.childElementCount - 1;
        let oldChild = scrolling_content.children[len-1];
        if(oldChild.tagName === 'STYLE'){
            scrolling_content.removeChild(oldChild); //remove old animation Style
        }

        let cssAnimation = document.createElement('style');
        cssAnimation.type = 'text/css';
        let rules = document.createTextNode(
            '@keyframes slideUp {'+'from { bottom: -' + height_scrolling_area + 'px; }'+ 'to { bottom: '+ height_scrolling_content + 'px; }'+ '}');
        cssAnimation.appendChild(rules);
        scrolling_content.appendChild(cssAnimation); //add new animation Style

    //update Animation Duration
        let duration_time = (height_scrolling_content / height_scrolling_area*6);
        console.log(duration_time);
        scrolling_content.style.animationDuration = `${duration_time}s`;
    };

    window.onload = fit_scroll_properties;
    window.onresize = fit_scroll_properties;
