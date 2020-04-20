from django.contrib import admin
from blog.models import Post, Category 
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
 
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin ) 
admin.site.register(Category, CategoryAdmin)
