from explorer.utils.finder.filenode import FileNode
from explorer.utils.finder.filetypes import FileTypes


# Unecessary for now
def load_file(path):
    """Returns FileNode object"""
    return FileNode(path)


def save_file(filenode, content, check=False):
    """Saves content of FileNode to related file and return True at the end.
    If check is True, then check for file to be properly saved and return
    True if so, otherwise False"""
    filenode._write(content)

    if filenode.type == FileTypes.TEXT:
        with open(filenode.abspath, 'w') as f:
            f.write(filenode.content)

    elif filenode.type == FileTypes.NONTEXT:
        with open(filenode.abspath, 'wb') as f:
            f.write(filenode.content)

    if check:
        if filenode.type == FileTypes.TEXT:
            with open(filenode.abspath, 'rt') as f:
                return f.read() == filenode.content
        elif filenode.type == FileTypes.NONTEXT:
            with open(filenode.abspath, 'rb') as f:
                return f.read() == filenode.content

    return True
