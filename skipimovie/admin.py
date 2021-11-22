from django.contrib import admin

from .models import Movie,browseMovie,Contact
admin.site.register(Movie)
admin.site.register(browseMovie)
admin.site.register(Contact)