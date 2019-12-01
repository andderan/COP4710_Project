from django.contrib import admin
from .models import Players, Team, Match, VideoGames

admin.site.site_header ='COP4710 Project Admin Page'
admin.site.index_title = 'Welcome to the Backend Control Termial'
admin.site.register(Players)
admin.site.register(Team)
admin.site.register(Match)
