from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Image
from .forms import ImageForm

# Create your views here.

# 首页视图 - 展示所有图片并提供上传表单
def home(request):
    images = Image.objects.all()
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '图片上传成功！')
            return redirect('home')
    else:
        form = ImageForm()
    
    return render(request, 'gallery/home.html', {
        'images': images,
        'form': form
    })

# 图片展示页 - 循环展示单张图片
def slideshow(request):
    images = Image.objects.all()
    return render(request, 'gallery/slideshow.html', {
        'images': images
    })
