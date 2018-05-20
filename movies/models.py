import json

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return '{}({})'.format(self.title, self.release_year)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    directed = models.ManyToManyField(Movie, related_name='directors', blank=True)
    acted = models.ManyToManyField(Movie, related_name='actors', blank=True)
    produced = models.ManyToManyField(Movie, related_name='producers', blank=True)
    aliases = models.CharField(max_length=500, blank=True)

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
