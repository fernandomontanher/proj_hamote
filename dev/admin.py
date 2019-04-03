from django.contrib import admin
from .models import Dev

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ['github_link', 'contact_link', 'profile_photo']
    list_display = ('project', 'availability')
    autocomplete_fields = ['project']

admin.site.register(Dev)

