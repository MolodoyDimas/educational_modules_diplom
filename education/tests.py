from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Module


class ModuleTestCase(APITestCase):

    def setUp(self) -> None:
        self.module = Module.objects.create(
            title='test'
        )

    def test_get_list(self):
        """
        Тестирование просмотра уроков
        """

        response = self.client.get(
            reverse('education:module-list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            [{'id': 1, 'sequence_number': None,
              'title': 'test', 'description': ''}])

    def test_module_create(self):
        """
        Тест создания модуля
        """

        data = {
            'title': 'test2',
            'description': 'test2',
        }

        response = self.client.post(
            reverse('education:module-create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            Module.objects.all().count(),
            2
        )

    def test_module_create_validation_error(self):
        """
        Тест ошибки валидации
        """

        data = {
            'title': '#@*-^',
            'description': 'test3'
        }

        response = self.client.post(
            reverse('education:module-create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


class ModuleTestCase2(APITestCase):

    def setUp(self):
        self.module = Module.objects.create(
            title='test',
            description='test'
        )

    def test_module_update(self):
        """
        Тестирование апдейта
        """

        url = reverse('education:module-update', kwargs={'pk': self.module.pk})

        data = {
            'title': self.module.title,
            'description': 'update_test'
        }

        response = self.client.put(url, data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {'id': self.module.id, 'sequence_number': None,
             'title': 'test', 'description': 'update_test'}
        )

    def test_module_delete(self):
        """
        Тестирование удаления
        """

        url = reverse('education:module-delete', kwargs={'pk': self.module.pk})

        response = self.client.delete(url)

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Module.objects.all().exists(),
        )
