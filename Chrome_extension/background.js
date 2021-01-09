chrome.browserAction.onClicked.addListener(function (tab) { //Fired when User Clicks ICON
    // Send request to server with...
    //sendRequest('http://localhost:8890?url=${tab.url}')
    console.log("Script exicuted!")
});