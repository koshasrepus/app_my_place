from django.db import models

class User(models.Model):
    """Пользователь Telegram"""
    chat_id = models.IntegerField()
    step = models.IntegerField()


class Palaces(models.Model):
    """Места"""
    title = models.CharField(max_length=100)
    place_lat = models.FloatField()
    place_lon = models.FloatField()
    image = models.ImageField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)