import os

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from explorer.utils import (
    normalize_path, get_paths, pdf_response, normalize_name)
from explorer.utils.filenode import FileNode
from explorer.utils.filetypes import FileTypes
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
        projects_dir = os.environ.get('FSEXPLORER_PROJECTS_DIRNAME', 'projects')
        context['in_projects_dir'] = filenode.name.lower() == projects_dir
        return render(request, 'explorer/finder.html', context)

    elif filenode.type == FileTypes.IMAGE:
        return render(request, 'explorer/media_page.html', context)

    elif filenode.type == FileTypes.TEXT:
        return render(request, 'explorer/editor.html', context)

    elif filenode.type == FileTypes.NONTEXT:
        messages.info(request, 'Please edit this file as Python\'s byte string')
        return render(request, 'explorer/editor.html', context)

    elif filenode.type == FileTypes.VIDEO:
        return render(request, 'explorer/media_page.html', context)

    elif filenode.type == FileTypes.PDF:
        return pdf_response(filenode)

    elif filenode.type == FileTypes.OTHER:
        messages.error(request, 'This file type is not supported')
        return render(request, 'explorer/editor.html', context)


def create_node(request, abspath):
    if request.method == 'GET':
        return redirect(reverse('node', kwargs={'abspath': abspath}))

    elif request.method == 'POST':
        abspath = normalize_path(abspath)

        file_name = normalize_name(request.POST.get('file_name'))
        folder_name = normalize_name(request.POST.get('folder_name'))
        resulting_path = os.path.join(abspath, file_name or folder_name)

        try:
            if file_name:
                open(resulting_path, 'x').close()
            elif folder_name:
                os.makedirs(resulting_path)
        except FileExistsError:
            messages.error(request, 'File with this name already exists')
        except Exception as e:
            messages.error(request, str(e))


        return redirect(reverse('node', kwargs={'abspath': abspath}))


def save_node(request, abspath):
    if request.method == 'GET':
        return redirect(reverse('node', kwargs={'abspath': abspath}))

    elif request.method == 'POST':
        filenode = FileNode(abspath)
        content = request.POST['content']
        save_file(filenode, content)
        return redirect(reverse('node', kwargs={'abspath': filenode.parent_node}))

    else:
        return HttpResponse('<p>This request method is not supported</p>')


def rename_node(request):
    if request.method == 'GET':
        return redirect(reverse('home'))

    elif request.method == 'POST':
        new_node_name = request.POST.get('node_name')
        abs_path = request.POST.get('abs_path')

        msg = 'Invalid or empty name provided'
        response = {
            'new_name': '',
            'success': False,
            'message': msg
        }

        if new_node_name and abs_path:
            node = FileNode(abs_path)

            try:
                node.rename(new_node_name)
                response = {
                    'new_name': node.name,
                    'success': True,
                    'message': '',
                }
            except Exception as e:
                response['message'] = str(e)

        else:
            response['message'] = msg

        return JsonResponse(response)

    else:
        return HttpResponse('<p>This request method is not supported</p>')


def remove_node(request):
    if request.method == 'GET':
        return redirect(reverse('home'))

    elif request.method == 'POST':
        abs_path = request.POST.get('abs_path')

        msg = 'No such file or directory or it is forbidden to remove'
        response = {
            'new_name': '',
            'success': False,
            'message': msg
        }

        if  abs_path:
            node = FileNode(abs_path)

            try:
                node.remove(safe=True) # !!!
                response = {
                    'success': True,
                    'message': '',
                }
            except Exception as e:
                response['message'] = str(e)

        else:
            response['message'] = msg

        return JsonResponse(response)

    else:
        return HttpResponse('<p>This request method is not supported</p>')


def image(request, img_path):
    with open(normalize_path(img_path), 'rb') as f:
        img = f.read()

    return HttpResponse(img, content_type='image/png')


def video(request, vid_path):
    from wsgiref.util import FileWrapper

    video_node = FileNode(vid_path)
    file = FileWrapper(open(video_node.abspath, 'rb'))

    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename={}'.format(video_node.name)

    return response
