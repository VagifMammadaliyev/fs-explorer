# FS-Explorer

App allows exploring your file system in browser.

### Features
1. Viewing your files and directories
2. Editing your files and directories content
3. Creating, renaming, removing your files and directories


### Which files can you view?

1. Images
2. Videos
3. PDF Documents
4. Text files (editable)
5. Non-text files in binary mode (editable)

### Additional stuff

1. ~You can open your projects' directories as project (with project tree displayed in your browser)~ **(not added yet)**
2. ~Tests passed~ **(not added yet)**
3. Convenient File System Nodes' Interface (FSN Interface)

## FSN Interface

Small wrapper around functions in ```os``` and ```shutil``` modules for manipulating file system of \*nix OS (Linux / macOS).

```python
from explorer.utils.filetypes import *
from explorer.utils.filenode import *

node = FileNode("/Users/vagifmammadaliyev/Desktop/file.txt")

node.rename("new-name.txt")
node.name # new-name.txt
node.parent_node # /Users/vagifmammadaliyev/Desktop
node.type # FileTypes.TEXT == 'text'
node.description # Plain Text file
node.remove(safe=True)

# and more in utils directory
```

Also in ```explorer.utils.utils``` (you can import it as ```from explorer.utils import *```) you'll find some functions for normalizing paths and file names and other useful functionality.

### Requirements
1. Django
2. Python 3

### Running

```bash
./manage.py runserver  # do it in fsexplorer directory
```

There are Django warnings. This app is not ready for production!
