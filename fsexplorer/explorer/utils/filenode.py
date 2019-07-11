import os
import shutil

from explorer.utils import utils
from explorer.utils.filetypes import FileTypes
from explorer.utils.errors.exceptions import (
    CannotWriteToThisFileType, UnsafeRemovalAttempt)


class FileNode:
    def __init__(self, abspath, to_list=False):
        abspath = utils.normalize_path(abspath)

        self.abspath = abspath
        self.name = self._get_name()
        self.parent_node = os.path.dirname(self.abspath)
        self.hidden = self.name[0] == '.'
        self.type = utils.determine_type(self.abspath)
        self.removed = False

        if self.type != FileTypes.FOLDER:
            self.description = utils.get_file_description(self.abspath)
        else:
            self.description = 'Folder'

        if not to_list:
            if self.type == FileTypes.FOLDER:
                self.content = [FileNode(os.path.join(self.abspath, item), to_list=True)
                                for item in os.listdir(self.abspath)]
                self._sort()
            elif self.type == FileTypes.IMAGE \
                or self.type == FileTypes.PDF \
                    or self.type == FileTypes.VIDEO:
                self.content = self.abspath
            elif self.type == FileTypes.NONTEXT or self.type == FileTypes.TEXT:
                self.content = utils.open_file(self.abspath, self.type)
            elif self.type == FileTypes.OTHER:
                self.content = '?'

    def rename(self, new_name):
        new_abs_path = utils.normalize_path(
            os.path.join(self.parent_node,
            utils.normalize_name(new_name)))
        os.rename(self.abspath, new_abs_path)
        self.abspath = new_abs_path
        self.name = self._get_name()
        return self.abspath

    def remove(self, *, safe=True):
        # Dangerous
        if safe:
            # Allow removing only visible files inside
            # home directory and each visible subdirectory
            home_dir_path = utils.normalize_path(os.environ["HOME"])
            print(home_dir_path)
            print(self.abspath  )
            if home_dir_path in self.abspath and \
                not self.name.startswith('.'):
                self._remove_unsafe()
            else:
                raise UnsafeRemovalAttempt("""Trying to remove hidden file or file not
                within home directory. This is considered unsafe. Better delete anything you want manually!
                """)
        else:
            self._remove_unsafe()

    def _remove_unsafe(self):
        """Removes files from system without ignoring errors occured
        This is for secutiry reasons and preventing accidentally removing
        important system files.

        This restriction must work on most *nix distributions"""
        if self.type == FileTypes.FOLDER:
            shutil.rmtree(self.abspath)
        else:
            os.remove(self.abspath)

        self.removed = True


    def _get_name(self):
        return self.abspath.split(os.path.sep)[-1]

    def _sort(self):
        if self.type == FileTypes.FOLDER:
            hiddens = sorted(
                        [node for node in self.content if node.hidden],
                        key=lambda x: x.name)
            non_hiddens = sorted(
                            [node for node in self.content if not node.hidden],
                            key=lambda x: x.name)
            self.content = non_hiddens + hiddens

    def _write(self, content):
        if not (self.type == FileTypes.IMAGE \
            or self.type == FileTypes.FOLDER \
                or self.type == FileTypes.VIDEO \
                    or self.type == FileTypes.PDF):
            self.content = content.replace('\r', '')
        else:
            raise CannotWriteToThisFileType(
                'Attempted to write to filenode with type: {}'
                    .format(self.type))

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<FileNode name={}; type={}>'.format(self.name, self.type)
