import os

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from explorer.utils.finder.filenode import FileNode
from explorer.utils.finder.filetypes import FileTypes


def home(request):
    homepath = os.path.join('Users', os.getlogin())
    return redirect(reverse('node', kwargs={'abspath': homepath}))


def node(request, abspath):
    filenode = FileNode(abspath)

    context = {
        'filenode': filenode,
        'username': os.getlogin(),
        'FileTypes': FileTypes,
    }

    return render(request, 'explorer/finder.html', context)
