from django.contrib import admin
from .models import Post


# Register your models here.
admin.site.register(Post)
class PostDB(admin.ModelAdmin):
    list_display = ["title","text","author","created_date","published_date"
        
    ]