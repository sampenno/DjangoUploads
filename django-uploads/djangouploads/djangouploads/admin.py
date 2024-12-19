from django.contrib import admin
from djangouploads.models import Movie

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Movie, MovieAdmin)

