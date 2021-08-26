from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Science,Teachers


class ScienceAdmin(ImportExportActionModelAdmin):
	list_display=('name','status',)
	list_filter = ('status',)
	search_fields=('name','status',)
	ordering=('status','name',)

class TeachersAdmin(ImportExportActionModelAdmin):
    list_display = ('full_name', 'birth_date', 'degree','grade', 'status')
    list_filter = ('status', 'grade', 'degree')
    search_fields = ('full_name', 'birth_date')
    ordering = ('grade', 'full_name')
    readonly_fields = ('get_photo',)
    save_as = True
    save_on_top = True

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50">')

    get_photo.short_description = "Photo"

admin.site.register(Science, ScienceAdmin)
admin.site.register(Teachers, TeachersAdmin)