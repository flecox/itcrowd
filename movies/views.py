from rest_framework import viewsets

from movies.models import Movie, Person
from movies.serializers import MovieSerializer, PersonSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Movies to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Persons to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
