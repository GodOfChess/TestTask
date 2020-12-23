from django.db import models
from geopy.geocoders import Nominatim
import folium



class Places(models.Model):
    title = models.CharField('Название', max_length=50)
    comment = models.CharField('Комментарий', max_length=250)
    t_lat = models.FloatField('Первая координата')
    t_lon = models.FloatField('Вторая координата')
    username = models.CharField('ID пользователя', max_length=50)

    @property
    def createmap(self):
        m = folium.Map(width=400, height=250)
        folium.Marker([self.t_lat, self.t_lon], icon=folium.Icon(color='purple')).add_to(m)
        m = m._repr_html_()
        return m

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Посещенное место'
        verbose_name_plural = 'Посещенные места'
