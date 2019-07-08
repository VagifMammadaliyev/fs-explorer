import os
from explorer.utils.finder import utils
from explorer.utils.finder.filetypes import FileTypes
from explorer.utils.errors.exceptions import CannotWriteToThisFileType


class FileNode:
    def __init__(self, abspath):
        abspath = utils.normalize_path(abspath)
        self.abspath = abspath
        self.name = self.abspath.split(os.path.sep)[-1]

        self.type = utils.determine_type(self.abspath)

        if self.type == FileTypes.FOLDER:
            self.content = os.listdir(self.abspath)
        elif self.type == FileTypes.IMAGE:
            self.content = self.abspath
        elif self.type == FileTypes.NONTEXT or self.type == FileTypes.TEXT:
            self.content = editor_utils.open_file(self.abspath, self.type)

        self.parent_node = os.path.dirname(self.abspath)

    def _write(self, content):
        if not (self.type == FileTypes.IMAGE or self.type == FileTypes.FOLDER):
            self.content = content
        else:
            raise CannotWriteToThisFileType(
                'Attempted to write to filenode with type: {}'
                    .format(self.type))
