from django.contrib import admin
from blog.models import BlogPost, BlogPostImage, Author

admin.site.register(BlogPost)
admin.site.register(BlogPostImage)
admin.site.register(Author)
