from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Image
from .forms import ImageForm, MultipleImageUploadForm

# Create your views here.

# 首页视图 - 展示所有图片并提供上传表单
def home(request):
    images = Image.objects.all()
    
    if request.method == 'POST':
        # 检查是否为多图片上传
        if 'images' in request.FILES:
            multi_form = MultipleImageUploadForm(request.POST)
            
            if multi_form.is_valid():
                description = multi_form.cleaned_data['description']
                
                # 获取上传的所有图片
                files = request.FILES.getlist('images')
                if files:
                    for image_file in files:
                        Image.objects.create(
                            description=description,
                            image=image_file
                        )
                    messages.success(request, f'成功上传 {len(files)} 张图片！')
                    return redirect('home')
                else:
                    messages.error(request, '请选择至少一张图片上传！')
            else:
                messages.error(request, '表单验证失败，请检查输入！')
        else:
            # 处理单图片上传
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, '图片上传成功！')
                return redirect('home')
    else:
        form = ImageForm()
        multi_form = MultipleImageUploadForm()
    
    return render(request, 'gallery/home.html', {
        'images': images,
        'form': form,
        'multi_form': multi_form
    })

# 图片展示页 - 循环展示单张图片
def slideshow(request):
    images = Image.objects.all()
    return render(request, 'gallery/slideshow.html', {
        'images': images
    })
