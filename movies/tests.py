from rest_framework import status
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class MoviesTestCase(TestCase):

    def setUp(self):
        super(MoviesTestCase, self).setUp()
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token = None

    def _login(self):
        data = {'username': 'testuser', 'password': '12345'}
        response = self.client.post('/api-token-auth/', data=data)
        self.token = response.data['token']

    def _create_person(self, first_name, last_name, aliases=None):
        data = {'first_name': first_name, 'last_name': last_name}
        if aliases:
            data['aliases'] = aliases

        response = self.client.post(reverse('person-list'), data=data, HTTP_AUTHORIZATION="JWT {}".format(self.token))
        return response.data['id']

    def test_add_person(self):
        # CREATE:
        # only logged in users can create or delete objects:
        data = {'first_name': 'Gonzalo', 'last_name': 'Almeida', 'aliases': ['the best', 'the worst']}
        response = self.client.post(reverse('person-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # now login
        self._login()

        response = self.client.post(reverse('person-list'), data=data, HTTP_AUTHORIZATION="JWT {}".format(self.token))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.data
        self.assertEqual(data['first_name'], 'Gonzalo')
        self.assertEqual(data['last_name'], 'Almeida')
        self.assertEqual(data['aliases'], ['the best', 'the worst'])

        # Get person information without being logged in:
        response = self.client.get(reverse('person-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data[0]['first_name'], 'Gonzalo')
        self.assertEqual(data[0]['last_name'], 'Almeida')
        self.assertEqual(data[0]['aliases'], ['the best', 'the worst'])
        person_id = data[0]['id']

        # UPDATE
        data = {'first_name': 'Emilio'}
        # try to update person with out being logged in:
        response = self.client.patch(reverse('person-detail', kwargs={'pk': person_id}), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # now logged in:
        response = self.client.patch(
            reverse('person-detail', kwargs={'pk': person_id}), data=data,
            HTTP_AUTHORIZATION="JWT {}".format(self.token))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data['id'], person_id)
        self.assertEqual(data['first_name'], 'Emilio')
        self.assertEqual(data['last_name'], 'Almeida')
        self.assertEqual(data['aliases'], ['the best', 'the worst'])

        # DELETE
        # now try to delete with out being logged in:
        response = self.client.delete(reverse('person-detail', kwargs={'pk': person_id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # now logged in:
        response = self.client.delete(
            reverse('person-detail', kwargs={'pk': person_id}), HTTP_AUTHORIZATION="JWT {}".format(self.token))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_add_movie(self):
        # CREATE:
        # only logged in users can create or delete objects:
        data = {
            'title': 'the return of Gonzalo II',
            'release_year': 1984,
        }
        response = self.client.post(reverse('person-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # now login
        self._login()
        # add a basic movie (no persons related)
        response = self.client.post(reverse('movie-list'), data=data, HTTP_AUTHORIZATION="JWT {}".format(self.token))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.data
        self.assertEqual(data['title'], 'the return of Gonzalo II')
        self.assertEqual(data['release_year'], 'MCMLXXXIV')

        # create 2 persons:
        first_person_id = self._create_person(
            first_name='Gonzalo', last_name='Almeida', aliases=['the best', 'the worst'])
        second_person_id = self._create_person(first_name='Sebastian', last_name='Norry')

        # create new movie with persons in it
        data = {
            'title': 'the return of Gonzalo II',
            'release_year': 1984,
            'directors': [first_person_id, second_person_id],
            'actors': [first_person_id, second_person_id],
            'producers': [first_person_id, second_person_id],
        }
        response = self.client.post(reverse('movie-list'), data=data, HTTP_AUTHORIZATION="JWT {}".format(self.token))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.data
        self.assertEqual(data['title'], 'the return of Gonzalo II')
        self.assertEqual(data['release_year'], 'MCMLXXXIV')

        # test persons information inside movie response:
        person_fields = ['directors', 'producers', 'actors']
        for field in person_fields:
            self.assertEqual(len(data[field]), 2)
            self.assertEqual(data[field][0]['first_name'], 'Gonzalo')
            self.assertEqual(data[field][0]['last_name'], 'Almeida')
            self.assertEqual(data[field][1]['first_name'], 'Sebastian')
            self.assertEqual(data[field][1]['last_name'], 'Norry')

        movie_id = data['id']

        # UPDATE
        data = {'release_year': 2018, 'directors': [second_person_id]}
        # try to update person with out being logged in:
        response = self.client.patch(reverse('movie-detail', kwargs={'pk': movie_id}), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # logged in:
        response = self.client.patch(
            reverse('movie-detail', kwargs={'pk': movie_id}), data=data, HTTP_AUTHORIZATION="JWT {}".format(self.token))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data['id'], movie_id)
        self.assertEqual(data['title'], 'the return of Gonzalo II')
        self.assertEqual(data['release_year'], 'MMXVIII')
        self.assertEqual(len(data['directors']), 1)

        # DELETE
        # try to delete with out being logged in:
        response = self.client.delete(reverse('movie-detail', kwargs={'pk': movie_id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # logged in:
        response = self.client.delete(
            reverse('movie-detail', kwargs={'pk': movie_id}), HTTP_AUTHORIZATION="JWT {}".format(self.token))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
