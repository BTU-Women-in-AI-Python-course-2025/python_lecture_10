from django.db import models


class BlogPost(models.Model):
    title = models.CharField(verbose_name='სათაური', max_length=255)
    text = models.TextField(verbose_name='ტექსტი')
    is_active = models.BooleanField(verbose_name='აქტიურია', default=True)
    created_at = models.DateTimeField(
        verbose_name='შექმნის თარიღი', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        verbose_name='განახლების თარიღი', auto_now=True, null=True)
    website = models.URLField(verbose_name='ვებ მისამართი', null=True)
    document = models.FileField(upload_to='blog_post_documents/', null=True)
    picture = models.ImageField(upload_to='blog_post_picture/', null=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['title', 'created_at']
        unique_together = [['title', 'text']]

    def __str__(self):
        return self.title


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
