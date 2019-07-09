import os

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from explorer.utils.finder.utils import normalize_path, get_paths
from explorer.utils.finder.filenode import FileNode
from explorer.utils.finder.filetypes import FileTypes
from explorer.utils.editor import save_file


def home(request):
    homepath = os.environ['HOME']
    return redirect(reverse('node', kwargs={'abspath': homepath}))


def node(request, abspath):
    filenode = FileNode(abspath)

    context = {
        'paths': get_paths(filenode),
        'filenode': filenode,
        'username': os.getlogin(),
        'FileTypes': FileTypes,
        'homepath': os.environ['HOME']
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


def save_node(request, abspath):
    if request.method == 'GET':
        return redirect(reverse('node', kwargs={'abspath': abspath}))
    elif request.method == 'POST':
        filenode = FileNode(abspath)
        content = request.POST['content']
        save_file(filenode, content)
        return redirect(reverse('node', kwargs={'abspath': filenode.parent_node}))


def image(request, img_path):
    with open(normalize_path(img_path), 'rb') as f:
        img = f.read()

    return HttpResponse(img, content_type='image/png')
