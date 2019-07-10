import os

from django.http import FileResponse

from explorer.utils.filetypes import FileTypes, descriptions
from explorer.utils.errors.exceptions import InvalidPath

_image_extensions = [
    '.tif', '.tiff', '.gif', 'jpeg', '.jpg', '.jif', '.jfif',
    '.jp2', '.jpx', '.j2k', '.j2c', '.fpx', '.pcd', '.png'
]

_video_extensions = [
    '.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
    '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv'
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


def get_paths(filenode):
    """Returns list of tuples with path chunk names and related absolute paths"""
    chunks = filenode.abspath.split(os.path.sep)
    if chunks[0] == '':
        chunks = chunks[1:]
    paths = []

    for i in range(len(chunks)):
        path = []
        for j in range(i + 1):
            path.append(chunks[j])
        path = normalize_path(os.path.sep.join(path))
        paths.append(path)

    return zip(chunks, paths)

def determine_type(path):
    """Returns file type as FileTypes object"""
    if os.path.isdir(path):
        return FileTypes.FOLDER
        
    else:
        for img_ext in _image_extensions:
            if path.endswith(img_ext):
                return FileTypes.IMAGE

        for vid_ext in _video_extensions:
            if path.endswith(vid_ext):
                return FileTypes.VIDEO

        if path.lower().endswith('.pdf'):
            return FileTypes.PDF

        try:
            _f = open(path, 'rt')
            _f.read()
            _f.close()
            return FileTypes.TEXT
        except UnicodeDecodeError:
            return FileTypes.NONTEXT
        except OSError:
            return FileTypes.OTHER


def get_file_description(path):
    filename = path.split(os.path.sep)[-1]

    for ext, desc in descriptions.items():
        if filename.lower().endswith(ext.lower()):
            return desc

    return filename[filename.rfind('.')+1:].upper() + ' file'


def open_file(path, type):
    """Returns file's content"""
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


def pdf_response(filenode):
    import io
    buffer = io.BytesIO(open_file(filenode.abspath, FileTypes.NONTEXT))
    return FileResponse(buffer, as_attachment=False, filename=filenode.name)
