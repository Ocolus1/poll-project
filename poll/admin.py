from django.contrib import admin
from .models import Poll

class PollAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "option_one", "option_two", "option_three")
    list_display_links = ("id", "question")


admin.site.register(Poll, PollAdmin)
