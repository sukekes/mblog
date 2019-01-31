from django.contrib import admin
from .models import Post   # 是 from .models

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')


admin.site.register(Post, PostAdmin)