function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var csrftoken = getCookie('csrftoken');


function createNodeForm(which) {
  document.getElementById('node-form').style.display = 'block'

  let input = document.getElementById('node-name-input')

  if (which == 'file') {
    document.getElementById('file-create-button').style.backgroundColor = 'white'
    document.getElementById('folder-create-button').style.backgroundColor = '#b1cdfa'
    input.setAttribute('name', 'file_name')
    input.setAttribute('placeholder', 'Enter new file name')
  } else if (which == 'folder') {
    document.getElementById('folder-create-button').style.backgroundColor = 'white'
    document.getElementById('file-create-button').style.backgroundColor = '#b1cdfa'
    input.setAttribute('placeholder', 'Enter new directory name')
    input.setAttribute('name', 'folder_name')
  }
}


function renameNodeForm(elem) {
  let nodeRow = elem.parentNode
  let fileNode = nodeRow.getElementsByTagName("a")[0]

  // !!!
  fileNode.style.display = "none"

  // hidden input
  let hiddenInput = document.createElement("input")
  hiddenInput.setAttribute("value", elem.getAttribute("abs-path"))
  hiddenInput.setAttribute("name", "abs_path")
  hiddenInput.setAttribute("id", "abs-path-input")
  hiddenInput.setAttribute("hidden", "")

  // new name input
  let input = document.createElement("input")
  input.setAttribute("name", "node_name")
  input.setAttribute("required", "")
  input.setAttribute("value", "")
  input.setAttribute("placeholder", elem.getAttribute("file-name"))
  input.setAttribute("maxlength", "200")
  input.setAttribute("id", "new-name-input")
  input.setAttribute("class", "form-button save nice-width rename-input focus-white")
  input.style.marginTop = "0"

  nodeRow.insertBefore(input, elem)
  nodeRow.insertBefore(hiddenInput, elem)


  // !!!
  let renameButtons = nodeRow.getElementsByTagName("button")

  renameButtons[0].innerText = "Apply"
  renameButtons[0].setAttribute("onclick", "renameNode(this)")

  renameButtons[1].innerText = "Cancel"
  renameButtons[1].setAttribute("onclick", "cancelForm(this)")
}


function cancelForm(elem) {
  let nodeRow = elem.parentNode
  let fileNode = nodeRow.getElementsByTagName("a")[0]

  fileNode.style.display = "block"

  /// ????
  let input = nodeRow.getElementsByTagName("input")[0]
  input.parentNode.removeChild(input)
  let input2 = nodeRow.getElementsByTagName("input")[0]
  input2.parentNode.removeChild(input2)

  let renameButtons = nodeRow.getElementsByTagName("button")
  renameButtons[0].innerText = "Rename"
  renameButtons[0].setAttribute("onclick", "renameNodeForm(this)")

  renameButtons[1].innerText = "Delete"
  renameButtons[1].setAttribute("onclick", "deleteNode(this)")
}


function renameNode(elem) {
  let nodeRow = elem.parentNode

  let newName = document.getElementById("new-name-input").value
  let oldPath = document.getElementById("abs-path-input").value

  data = {
    "node_name": newName,
    "abs_path": oldPath,
    "csrfmiddlewaretoken": csrftoken,
  }


  $.ajax({
    type: "POST",
    url: elem.getAttribute("action-url"),
    data: data,
    success: function (response) {
      if (response["success"]) {
        cancelForm(elem)
        let fileNode = nodeRow.getElementsByClassName("nodename")[0]
        console.log(response["new_name"])
        fileNode.innerText = response["new_name"]
        elem.setAttribute("file-name", response["new_name"])
      } else {
        notify(response["message"])
      }
    },
  });
}


function deleteNode(elem) {
  let nodeRow = elem.parentNode
  let clickCount = elem.getAttribute("click-count")

  if (clickCount == "0") {
    elem.innerText = "REALLY?"
    elem.setAttribute("click-count", "1")

    setTimeout(() => {
      elem.innerText = "Delete"
      elem.setAttribute("click-count", "0")
    }, 3000)
  } else if (clickCount == "1") {
    data = {
      "abs_path": elem.getAttribute("abs-path"),
      "csrfmiddlewaretoken": csrftoken,
    }
    elem.innerText = "Deleting..."

    $.ajax({
      type: "POST",
      url: elem.getAttribute("action-url"),
      data: data,
      success: function (response) {
        if (response["success"]) {
          nodeRow.parentNode.removeChild(nodeRow)
        } else {
          notify(response["message"])
        }
      },
    });

  }

}


function notify(message) {
  let createNodeDiv = document.getElementsByClassName("create-node")[0]
  let messagePara = document.createElement("p")
  messagePara.setAttribute("class", "message error")
  messagePara.innerText = message
  let mainDiv = document.getElementsByTagName("main")[0]
  mainDiv.insertBefore(messagePara, createNodeDiv)

  window.scrollTo(0, 0)

  setTimeout(() => {
    messagePara.style.display = "none"
  }, 10000)
}
