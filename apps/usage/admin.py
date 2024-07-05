from django.contrib import admin
from .models import Usage

# Register your models here.

class UsageAdmin(admin.ModelAdmin):
    list_display = ('username', 'media_id', 'start_date', 'end_date')
    list_filter = ('username', 'media_id')

admin.site.register(Usage)
