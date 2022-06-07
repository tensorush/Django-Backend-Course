import os
import random
import urllib3

from faker import Faker
from django.test import Client, TestCase


class CategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_get(self):
        num_tests = 100
        faker = Faker()
        field_names = ['name']
        for i in range(num_tests):
            data = {'name': faker.name()}
            response = self.client.post('/api/category/', data)
            content = response.data
            self.assertTrue('id' in content)
            self.assertTrue('status' in content)
            self.assertTrue(content['status'] == 'OK')

            category_id = content['id']
            response = self.client.get('/api/category/' + str(category_id) + '/')
            content = response.data
            self.assertTrue('id' in content)

            for field in field_names:
                self.assertTrue(field in content)

    def tearDown(self):
        pass


class SystemViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_get(self):
        num_tests = 100
        http = urllib3.PoolManager()

        path_to_logos = './static/images/'
        logo_paths = os.listdir(path_to_logos)
        num_logos = len(logo_paths)

        faker = Faker()
        field_names = ['name', 'logo']
        for i in range(num_tests):
            data = {'name': faker.sentence(nb_words=random.randint(2, 4), ext_word_list=None),
                    'logo': open(path_to_logos + logo_paths[i % num_logos], 'rb')}

            response = self.client.post('/api/system/', data)
            content = response.data
            self.assertTrue('id' in content)
            self.assertTrue('status' in content)
            self.assertTrue(content['status'] == 'OK')

            system_id = content['id']
            response = self.client.get('/api/system/' + str(system_id) + '/')
            content = response.data
            self.assertTrue('id' in content)

            for field in field_names:
                self.assertTrue(field in content)
            self.assertTrue('logo' in content)

    def tearDown(self):
        pass
