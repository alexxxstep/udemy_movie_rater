from django.contrib import admin
from .models import Movie, Rating, Actor

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Actor)

