from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Image
from .forms import ImageForm, MultipleImageUploadForm

# Create your views here.

# 首页视图 - 展示所有图片并提供上传表单
def home(request):
    # 初始化变量，确保在所有执行路径中都有定义
    images = Image.objects.all()
    form = ImageForm()
    multi_form = MultipleImageUploadForm()
    
    if request.method == 'POST':
        # 检查请求中是否包含多图片上传的文件字段
        if 'images' in request.FILES:
            # 处理多图片上传
            multi_form = MultipleImageUploadForm(request.POST)
            files = request.FILES.getlist('images')
            
            if not files:
                messages.error(request, '请选择至少一张图片上传！')
            elif multi_form.is_valid():
                description = multi_form.cleaned_data['description']
                
                # 创建图片记录
                for image_file in files:
                    Image.objects.create(
                        description=description,
                        image=image_file
                    )
                messages.success(request, f'成功上传 {len(files)} 张图片！')
                return redirect('home')
            else:
                messages.error(request, '表单验证失败，请检查输入！')
        else:
            # 处理单图片上传
            form = ImageForm(request.POST, request.FILES)
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request, '图片上传成功！')
                    return redirect('home')
                else:
                    messages.error(request, '表单验证失败，请检查输入！')
            except Exception as e:
                messages.error(request, f'上传过程中发生错误: {str(e)}')
    
    # 渲染模板，确保所有变量都已定义
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
