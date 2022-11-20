from django.contrib import admin

from screens import models


@admin.register(models.Screen)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'message']
    list_display_links = ['pk', 'message']
