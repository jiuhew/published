from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('title', 'description')
    readonly_fields = ('uploaded_at',)
