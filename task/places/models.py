from django.db import models

class Places(models.Model):
    title = models.CharField('Название', max_length=50)
    comment = models.CharField('Комментарий', max_length=250)
    coordinates = models.FloatField('Координаты')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Посещенное место'
        verbose_name_plural = 'Посещенные места'
