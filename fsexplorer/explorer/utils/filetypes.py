class FileTypes:
    FOLDER = 'folder'   # directory nodes
    IMAGE = 'image'     # file names with image file extensions
    VIDEO = 'video'     # file names with video file extensions
    PDF = 'pdf'         # PDF file
    NONTEXT = 'nontext' # mostly binary files. in fact: files that
                        # cannot be decoded to utf-8 or if file is not
                        # of other type provided in this class
    TEXT = 'text'       # all files that can be edited as text
    OTHER = 'other'     # other filetypes that cannot be opened straight


descriptions = {
    # Audio
    '.aif': 'AIF audio file',
    '.cda': 'CD audio track file',
    '.mid': 'MIDI audio file',
    '.midi': 'MIDI audio file',
    '.mp3': 'MP3 audio file',
    '.mpa': 'MPEG-2 audio file',
    '.ogg': 'Ogg Vorbis audio file',
    '.wav': 'WAV file',
    '.wma': 'WMA audio file',
    '.wpl': 'Windows Media Player playlist',

    # Compressed
    '.7z': '7-Zip compressed file',
    '.arj': 'ARJ compressed file',
    '.deb': 'Debian software package',
    '.pkg': 'Package file',
    '.rar': 'RAR file',
    '.rpm': 'Red Hat Package Manager',
    '.tar.gz': 'Tarball compressed file',
    '.z': 'Z compressed file',
    '.zip': 'Zip compressed file',

    # Disc and media
    '.bin': 'Binary disc image',
    '.dmg': 'macOS X disc image',
    '.iso': 'ISO disc image',
    '.toast': 'Toast disc image',
    '.vcd': 'Virtual CD',

    # Data and database
    '.csv': 'Comma separated value file',
    '.dat': 'Data file',
    '.db': 'Database file',
    '.dbf': 'Database file',
    '.log': 'Log file',
    '.mdb': 'Microsoft Access database file',
    '.sav': 'Save file',
    '.sql': 'SQL database file',
    '.tar': 'Linux/Unix tarball file archive',
    '.xml': 'XML file',

    # Executable
    '.apk': 'Android package file',
    '.bat': 'Batch file',
    '.bin': 'Binary file',
    '.cgi': 'Perl script file',
    '.pl': 'Perl script file',
    '.com': 'MS-DOS command file',
    '.exe': 'Executable file',
    '.app': 'macOS application',
    '.gadget': 'Windows gadget',
    '.jar': 'Java archive file',
    '.py': 'Python file',
    '.wsf': 'Windows Script file',

    # Font
    '.fnt': 'Windows font file',
    '.fon': 'Generic font file',
    '.otf': 'Open type font file',
    '.ttf': 'TrueType font file',

    # Image
    '.ai': 'Adobe Illustrator file',
    '.bmp': 'Bitmap image',
    '.gif': 'GIF image',
    '.ico': 'Icon file',
    '.jpeg': 'JPEG file',
    '.jpg': 'JPEG file',
    '.png': 'PNG image',
    '.ps': 'PostScript file',
    '.psd': 'PSD image',
    '.svg': 'Scalable Vector Graphics file',
    '.tif': 'TIFF image',
    '.tiff': 'TIFF image',

    # Internet related
    '.asp': 'Active Server Page file',
    '.aspx': 'Active Server Page file',
    '.cer': 'Internet security certificate',
    '.css': 'Cascading Style Sheet file',
    '.htm': 'HTML file',
    '.html': 'HTML file',
    '.js': 'JavaScript file',
    '.jsp': 'Java Server Page file',
    '.part': 'Partially downloaded file',
    '.php': 'PHP file',
    '.rss': 'RSS file',
    '.xhtml': 'XHTML file',

    # Presentation
    '.key': 'Keynote presentation',
    '.odp': 'OpenOffice Impress presentation file',
    '.pps': 'PowerPoint slide show',
    '.ppt': 'PowerPoint presentation',
    '.pptx': 'PowerPoint Open XML presentation',

    # Programming
    '.lib': 'Library file',
    '.so': 'Library file',
    '.c': 'C source code file',
    '.cs': 'C# source code file',
    '.swift': 'Swift source code file',
    '.class': 'Java class file',
    '.cpp': 'C++ source code file',
    '.cs': 'Visual C# source code file',
    '.h': 'C, C++, and Objective-C header file',
    '.java': 'Java Source code file',
    '.sh': 'Bash shell script',
    '.vb': 'Visual Basic file',

    # Spreadsheet
    '.ods': 'OpenOffice Calc spreadsheet file',
    '.xlr': 'Microsoft Works spreadsheet file',
    '.xls': 'Microsoft Excel file',
    '.xlxs': 'Microsoft Excel Open XML spreadsheet file',

    # System
    '.bak': 'Backup file',
    '.cab': 'Windows Cabinet file',
    '.cfg': 'Configuration file',
    '.cpl': 'Windows Control panel file',
    '.cur': 'Windows cursor file',
    '.dll': 'DLL file',
    '.dmp': 'Dump file',
    '.drv': 'Device driver file',
    '.icns': 'macOS X icon resource file',
    '.ini': 'Initialization file',
    '.lnk': 'Windows shortcut file',
    '.msi': 'Windows installer package',
    '.sys': 'Windows system file',
    '.tmp': 'Temporary file',
    '.DS_Store': 'macOS Finder related file',

    # Word processors
    '.doc': 'Microsoft Word file',
    '.docx': 'Microsoft Word file',
    '.odt': 'OpenOffice Writer document file',
    '.rtf': 'Rich Text Format',
    '.tex': 'A LaTeX document file',
    '.txt': 'Plain text file',
    '.wks': 'Microsoft Works file',
    '.wps': 'Microsoft Works file',
    '.wpd': 'WordPerfect document',
}
