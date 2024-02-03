from django.contrib import admin
from .models import Project, Comment #, Tag
# Register your models here.

@admin.register(Project)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'rating', 'tags', 'updated_at'] 
    list_filter = ['public', 'title', 'tags'] 
    search_fields = ['title', 'description']
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ['author'] 
    # date_hierarchy = 'publish' 
    # ordering = ['status', 'publish']

admin.site.register(Comment)
# admin.site.register(Tag)