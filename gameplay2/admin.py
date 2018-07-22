from django.contrib import admin

# Register your models here.
from .models import Game, move

#admin.site.register(Game)

@admin.register(Game)
class GameAdm(admin.ModelAdmin):
    list_display = ('id','first_player','second_player','status')
    list_editable = ('status','first_player')
admin.site.register(move)
