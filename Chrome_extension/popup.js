var query = { active: true, currentWindow: true };
chrome.tabs.query(query, function (tab) {
    var puppy = document.getElementById('gif')
    var texty = document.getElementById('text')
    const xhr = new XMLHttpRequest(),
    method = "GET",
    url = "http://localhost:8080/?url=" + tab[0].url ;

  xhr.open(method, url, true);
  xhr.onreadystatechange = function () {
    // In local files, status is 0 upon success in Mozilla Firefox
    if (xhr.readyState === XMLHttpRequest.DONE) {
      var status = xhr.status;
      if (status === 0 || (status >= 200 && status < 400)) {
        // The request has been completed successfully
        var responded_stuff = xhr.responseText
        console.log(responded_stuff);
        puppy.remove()
        texty.innerText = responded_stuff
        texty.style.width = "250px"
        texty.style.wordWrap = "break-word"    
      } else {
        // Oh no! There has been an error with the request!
      }
    }
  };
  xhr.send();
})
