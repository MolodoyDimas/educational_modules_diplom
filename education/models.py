from django.db import models


class Module(models.Model):
    sequence_number = models.IntegerField(verbose_name='Порядковый номер',
                                          null=True)
    title = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'
