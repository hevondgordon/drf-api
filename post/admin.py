from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = (
        'caption',
        'like_count',
        'created_by',
        'service',
        # 'liked_by',
        'media_url',
        'media_type',
    )

    list_display = fields

admin.site.register(Post, PostAdmin)
