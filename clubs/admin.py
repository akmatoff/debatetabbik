from django.contrib import admin
from .models import Club, ClubJoinRequest

# Register your models here.
class ClubsAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'rating', 'is_approved')

class ClubJoinRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'club', 'is_approved')

admin.site.register(Club, ClubsAdmin)
admin.site.register(ClubJoinRequest, ClubJoinRequestAdmin)