from django.db import models


class Catalog(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name='Название каталога'
    )
    
    text = models.TextField(
        verbose_name='Markdown редактор'
    )

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self):
        return self.name
