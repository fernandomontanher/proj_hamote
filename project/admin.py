from django.contrib import admin
from .models import Project, Post, Skill

class PostInline(admin.StackedInline):
    model = Post
    extra = 1

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ['skill']
    list_display = ('project', 'availability')
    autocomplete_fields = ['project']



class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = [PostInline]



admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Skill,)