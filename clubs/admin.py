from django.contrib import admin
from .models import Club

# Register your models here.
class ClubsAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'rating')

admin.site.register(Club, ClubsAdmin)