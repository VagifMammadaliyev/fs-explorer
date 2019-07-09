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

    if filenode.type == FileTypes.FOLDER:
        return render(request, 'explorer/finder.html', context)
    elif filenode.type == FileTypes.IMAGE:
        return render(request, 'explorer/media_page.html', context)
    elif filenode.type == FileTypes.TEXT or filenode.type == FileTypes.NONTEXT:
        return render(request, 'explorer/editor.html', context)
    elif filenode.type == FileTypes.OTHER:
        context['message'] = 'This file type is not supported'
        return render(request, 'explorer/editor.html', context)


def image(request, img_path):
    with open(os.path.sep + img_path, 'rb') as f:
        img = f.read()

    return HttpResponse(img, content_type='image/png')
