from django.contrib import admin
from blog.models import Post
#from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

# Apply summernote to all TextField in model.
"""
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
"""

"""
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
"""

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'modify_date')
    list_filter   = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)


