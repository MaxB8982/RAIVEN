var popuphtml = 'puppy'
//`<!DOCTYPE html>
//<html>
    //<head>
        //<style>
            //button {
                //height: 100px;
                //width: 100px;
                //outline: none;
            //}
        //</style>
    //</head>
    //<body>
        //<p>
            //puppy
        //</p>
    //</body>
//</html>`
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
        var responded_stuff = xhr.responseText
        console.log(responded_stuff);
        var newhtml = popuphtml.replace('puppy', responded_stuff)
                
      } else {
        // Oh no! There has been an error with the request!
      }
    }
  };
  xhr.send();
});
