
from django.contrib import admin

from .models import Person, Movie

class PersonInline(admin.TabularInline):
    model = Person


class MovieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie)
admin.site.register(Person)
