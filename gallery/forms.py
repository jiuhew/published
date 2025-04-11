from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入标题'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '请输入描述（可选）', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': '标题',
            'description': '描述',
            'image': '选择图片'
        } 