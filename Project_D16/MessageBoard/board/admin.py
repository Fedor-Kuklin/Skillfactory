from django.contrib import admin
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentAd', 'commentUser', 'dateCreation', 'text', 'status_remove', 'status_add')
    list_filter = ('status_remove', 'status_add', 'dateCreation')
    search_fields = ('commentUser', 'text')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Ad)
