from django.contrib import admin
from bookmark.models import bookmark

# Register your models here.

class bookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link')
    ordering = ['id']

admin.site.register(bookmark, bookmarkAdmin)