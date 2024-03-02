from django.contrib import admin

# Register your models here.
from .models import Pdf

@admin.register(Pdf)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title' ,'created_on')
    search_fields = ('title','created_on')