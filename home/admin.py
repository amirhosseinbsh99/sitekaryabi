from django.contrib import admin
from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('Username', 'body','created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('Username', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


# Register your models here.
