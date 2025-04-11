from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='标题')
    description = models.TextField(blank=True, verbose_name='描述')
    image = models.ImageField(upload_to='images/', verbose_name='图片')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')
    
    def __str__(self):
        return self.title if self.title else f"图片-{self.id}"
    
    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'
        ordering = ['-uploaded_at']  # 按上传时间倒序排列
