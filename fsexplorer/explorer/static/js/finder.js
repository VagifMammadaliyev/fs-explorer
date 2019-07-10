function createNodeForm(which) {
  document.getElementById('node-form').style.display = 'block'

  let input = document.getElementById('node-name-input')

  if (which == 'file') {
    document.getElementById('file-create-button').style.backgroundColor = 'white'
    document.getElementById('folder-create-button').style.backgroundColor = '#b1cdfa'
    input.setAttribute('name', 'file_name')
  } else if (which == 'folder') {
    document.getElementById('folder-create-button').style.backgroundColor = 'white'
    document.getElementById('file-create-button').style.backgroundColor = '#b1cdfa'
    input.setAttribute('name', 'folder_name')
  }
}
