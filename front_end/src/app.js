// // import fetch from "node-fetch";
//
//
// // function parseCoupons(){
//
// //     // document.write();
//
// //     var display = document.createElement('div');
// //     display.innerHTML = "<div> AAAAAAAAAAAAAAAAAAAAAAAA </div>";
// //     document.body.appendChild(display);
//
// //   }
//
// // parseCoupons()
//
// let a = fetch('home.html')
// // .then((text) => {
// //     const otherDoc = document.implementation.createHTMLDocument("Foo").documentElement;
// //     otherDoc.innerHTML = text;
// //     document.querySelector(".element_on_main_page").textContent = otherDoc.querySelector(".awesome_external_element").textContent;
// alert(a)

var clickedEl = null;

function getText( obj ) {
    return obj.textContent ? obj.textContent : obj.innerText;
}

document.addEventListener("contextmenu", function(event){
    clickedEl = event.target;
    console.log(typeof(clickedEl))
    console.log(getText(clickedEl))

    chrome.storage.sync.set({
        "selection_context": getText(clickedEl)
    })

    // chrome.storage.sync.set({
    //     "document_context": getText(document.)
    // })
    //
    // console.log(getText(document))

}, true);

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if(request == "getClickedEl") {
        sendResponse({value: clickedEl.value});
    }
});
