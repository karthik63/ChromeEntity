// import fs from 'fs';

var linkme_contextmenu = {
    "id": "link_me",
    "title": "link_me",
    "contexts": ["selection"]
}

async function getCurrentTab() {

    let queryOptions = { active: true, currentWindow: true };
    var tab = 'kk'
    await chrome.tabs.query(queryOptions, function(tabs) {
        var currentTab = tabs[0];
        console.log(currentTab);
        tab = currentTab;
        return currentTab;
    });

    console.log(tab);
    return tab;
}

chrome.contextMenus.create(linkme_contextmenu);

async function find(info, tab){

    let elt = null

    await chrome.tabs.sendMessage(tab.id, "getClickedEl", {frameId: info.frameId}, data => {
        console.log(data.value)
        elt.value = data.value;
        console.log(data.value);
    });
}

async function mycallback(info) {

    let elt = null


    chrome.tabs.query({active: true, currentWindow: true},function(tabs) {
        console.log(tabs)
        chrome.tabs.sendMessage(tabs[0].id, "getClickedEl", {frameId: info.frameId}, function(response) {
            console.log(response);
        });
    });


}

chrome.contextMenus.onClicked.addListener(function (click_object){
    
    // alert(click_object.selectionText);
    let selection_text = click_object.selectionText;
    if (click_object.menuItemId == "link_me" && selection_text){

        console.log(click_object)

        chrome.storage.sync.set({
            "selection_text": selection_text
        });

        chrome.storage.sync.set({
            "url": click_object.pageUrl
        });

        mycallback(click_object)

        // chrome.windows.create({'url': 'src/home.html', 'type': 'popup', 'width': 100, "height": 100, "left": 10, "top": 10}, function(window) {
        chrome.windows.create({'url': 'src/home.html', 'type': 'popup', 'width': 400, "height": 800, }, function(window) {
        });



    }
    // alert(click_object);



});

