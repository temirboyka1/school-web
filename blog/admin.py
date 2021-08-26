from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish','status', 'get_photo')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body', 'author')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    readonly_fields = ('views', 'publish', 'created', 'updated', 'get_photo')
    fields = ('title', 'slug', 'author', 'body', 'image', 'get_photo','category', 'views', 'publish', 'created', 'updated', 'status', 'tags', )
    save_as = True
    save_on_top = True

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50">')

    get_photo.short_description = "Photo"

admin.site.register(Post, PostAdmin)