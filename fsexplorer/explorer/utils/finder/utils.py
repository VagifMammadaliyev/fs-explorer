import os
from explorer.utils.finder.filetypes import FileTypes
from explorer.utils.errors.exceptions import InvalidPath

_image_extensions = [
    '.tif', '.tiff', '.gif', 'jpeg', '.jpg', '.jif', '.jfif',
    '.jp2', '.jpx', '.j2k', '.j2c', '.fpx', '.pcd', '.png'
]

def normalize_path(path):
    """Add / where neccesary then pass to os.path.normpath"""
    try:
        if path[0] != os.path.sep:
            path = os.path.sep + path
    except IndexError:
        raise InvalidPath('Empty path provided')

    path = path if path[-1] != os.path.sep else path[:-1]

    return os.path.normpath(path)


def determine_type(path):
    """Returns file type as FileTypes object"""
    if os.path.isdir(path):
        return FileTypes.FOLDER
    else:
        for img_ext in _image_extensions:
            if path.endswith(img_ext):
                return FileTypes.IMAGE

        try:
            _f = open(path, 'rt')
            _f.read()
            _f.close()
            return FileTypes.TEXT
        except UnicodeDecodeError:
            return FileTypes.NONTEXT
        except OSError:
            return FileTypes.OTHER


def open_file(path, type):
    if type == FileTypes.TEXT:
        with open(path, 'rt') as f:
            content = f.read()
        return content

    elif type == FileTypes.NONTEXT:
        with open(path, 'rb') as f:
            content = f.read()
        return content

    else:
        return 'Something went wrong!'
