from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = (
        'caption',
        # 'is_liked',
        'created_by',
        'service',
        # 'liked_by',
        'media_url',
        'media_type',
    )

    list_display = fields

admin.site.register(Post, PostAdmin)
