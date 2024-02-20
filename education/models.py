from django.db import models


class Module(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'