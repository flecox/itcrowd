import json

from django.db import models

from movies.utils import to_roman


class Movie(models.Model):
    title = models.CharField(max_length=200, help_text='Movie title')
    release_year = models.PositiveIntegerField(help_text='Moview release year')

    def __str__(self):
        return '{}({})'.format(self.title, to_roman(self.release_year))


class Person(models.Model):
    first_name = models.CharField(max_length=30, help_text='Persons first name')
    last_name = models.CharField(max_length=30, help_text='Person Last name')
    directed = models.ManyToManyField(
        Movie, related_name='directors', blank=True, help_text='Movies this person directed')
    acted = models.ManyToManyField(Movie, related_name='actors', blank=True, help_text='Movies this person acted in')
    produced = models.ManyToManyField(
        Movie, related_name='producers', blank=True, help_text='Movies this person produced')
    aliases = models.CharField(max_length=500, blank=True, help_text='Person aliases')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_aliases(self):
        if self.aliases:
            return json.loads(self.aliases)

    def set_alias(self, al):
        aliases = json.loads(self.aliases or '[]')
        if al not in aliases:
            aliases.append(al)
            self.aliases = json.dumps(aliases)
            self.save()
