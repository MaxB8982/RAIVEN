chrome.browserAction.onClicked.addListener(function (tab) {
  //Fired when User Clicks ICON
  console.log("Script exicuted!");
  const xhr = new XMLHttpRequest(),
    method = "GET",
    url = "http://localhost:8080/?url=" + tab.url ;

  xhr.open(method, url, true);
  xhr.onreadystatechange = function () {
    // In local files, status is 0 upon success in Mozilla Firefox
    if (xhr.readyState === XMLHttpRequest.DONE) {
      var status = xhr.status;
      if (status === 0 || (status >= 200 && status < 400)) {
        // The request has been completed successfully
        returnedstuff = xhr.responseText
        console.log(returnedstuff);
      } else {
        // Oh no! There has been an error with the request!
      }
    }
  };
  xhr.send();
});
