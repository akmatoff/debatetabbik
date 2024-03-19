from django.contrib import admin
from .models import Club

# Register your models here.
class ClubsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Club, ClubsAdmin)