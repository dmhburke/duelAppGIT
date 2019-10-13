from django.contrib import admin

# Register your models here.

from catalog.models import PlayerModel

# Define new admin class - PLAYER
class PlayerModelAdmin(admin.ModelAdmin):
     list_display = ('number', 'name', 'HC','total',)
     ordering = ('-total', 'number',)

# Register admin class
admin.site.register(PlayerModel, PlayerModelAdmin)
