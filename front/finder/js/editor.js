function focusOnInput() {
  document.getElementById("editor-input").focus()
  window.scrollTo(0, document.getElementById("editor").offsetTop - 10)
}


function escapeHtml(unsafe) {
  return unsafe
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}


function writeEditor(editor, text) {
  // inserts next text into editor
  // returns change in length of editor content
  let oldText = editor.innerText
  editor.innerText = text

  return text.length - oldText.length
}


function drawCursor(editor, at) {
  // draws cursor at a given position in editor
  at--
  let text = editor.innerText
  let cursoredText = ""

  if (at == text.length) {
    cursoredText = escapeHtml(text) + "<span class='empty-cursor' id='cursor'></span>"
  } else {
    cursoredText = replaceLetter(text, at)
  }

  editor.innerHTML = cursoredText

  return document.getElementById("cursor")
}


function replaceLetter(text, index) {
  // replaces letter style with cursor style imitating cursor
  let tag = "<span id='cursor'>"
  if (text[index] == '\n') {
    tag = "<span class='empty-cursor' id='cursor'>"
  }
  let cursoredLetter = tag + escapeHtml(text[index]) + "</span>"
  return escapeHtml(text.substr(0, index)) + cursoredLetter + escapeHtml(text.substr(index + 1, text.length))
}


function editorType(e=null) {
  // insert to editor
  let editor = document.getElementById("editor")
  let input = document.getElementById("editor-input")

  let advance = writeEditor(editor, input.value)
  input.setAttribute("cursor-position", input.selectionEnd + 1)

  // draw cursor
  let cursor = drawCursor(editor, input.selectionEnd + 1)

  // scroll to cursor
  editor.scrollTo(cursor.offsetLeft - editor.offsetLeft - 10, cursor.offsetTop - editor.offsetTop - 10)
}

// initial inserting input content
editorType()
