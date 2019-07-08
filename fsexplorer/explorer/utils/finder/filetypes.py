class FileTypes:
    FOLDER = 'folder'   # directory nodes
    IMAGE = 'image'     # file names with image file extensions
    NONTEXT = 'nontext' # mostly binary files. in fact: files that
                        # cannot be decoded to utf-8 or if file is not
                        # of other type provided in this class
    TEXT = 'text'       # all files that can be edited as text
    OTHER = 'other'     # other filetypes, such as disk images, etc.
