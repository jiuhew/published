from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'description', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('title', 'description')
    readonly_fields = ('uploaded_at',)
    
    def get_title(self, obj):
        return obj.title if obj.title else f"图片-{obj.id}"
    get_title.short_description = '标题'
