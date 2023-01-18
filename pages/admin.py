from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'designation', 'created_at', 'thumbnail')
    list_display_links = ('first_name', 'last_name', 'thumbnail')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" width="100" style="border-radius: 50%;">')

    thumbnail.short_description = 'Photo'
