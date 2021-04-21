from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ModelForm
from .models import Blog


# Create your views here.


def fun(request):
    data = Blog.objects.all()
    return render(request, "blog.html", {'data': data})


def detail(request, id):
    obj = Blog.objects.get(id=id)
    return render(request, "details.html", {'obj': obj})


def update(request, id):
    obj1 = Blog.objects.get(id=id)
    form = ModelForm(request.POST or None, request.FILES, instance=obj1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "edit.html", {'form': form, 'obj1': obj1})

def delete(request,id):
    if request.method=='POST':
        obj1=Blog.objects.get(id=id)
        obj1.delete()
        return redirect('/')
    return render(request,"delete.html")