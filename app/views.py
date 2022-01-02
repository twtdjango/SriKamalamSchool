from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def home(request):
    context = {}
    context['images'] = Image.objects.all()
    context['videos'] = Video.objects.all()
    return render(request, 'index.html', {'context': context})


def about(request):
    context = {'images': Image.objects.all()}
    # print(context['images'])
    return render(request, 'about.html', {'context': context})


def contactus(request):
    if request.method == 'POST':
        Feedback.objects.create(
            Name=request.POST['Name'],
            Email=request.POST['Email'],
            Contact=request.POST['Contact'],
            Message=request.POST['Message']
        )
        return redirect('/contactus')
    return render(request, 'contact.html')


def application(request):
    if request.method == 'POST':
        Application.objects.create(
            Name=request.POST['Name'],
            Email=request.POST['Email'],
            Contact=request.POST['Contact'],
            Message=request.POST['Message']
        )
        return redirect('/application')
    return render(request, 'application.html')


def image_gallery(request):
    context = {'images': Image.objects.all()}
    # print(context['images'])
    return render(request, 'image_gallery.html', {'context': context})


def video_gallery(request):
    context = {'videos': Video.objects.all()}
    return render(request, 'video_gallery.html', {'context': context})


def teachers(request):
    return render(request, 'teacher_details.html')
