from django.db import models
from django.conf import settings


class Bus(models.Model):
    number = models.CharField(max_length=10, verbose_name='Номер автобуса', unique=True)
    capacity = models.IntegerField(verbose_name='Вместимость')

    # Другие поля, если необходимо

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобусы'


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название города', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Route(models.Model):
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city',
                                       verbose_name='Город отправления')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city',
                                     verbose_name='Город прибытия')

    def __str__(self):
        return f'{self.departure_city} - {self.arrival_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


class Trip(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, verbose_name='Автобус')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Маршрут')
    departure_time = models.DateTimeField(verbose_name='Время отправления')
    arrival_time = models.DateTimeField(verbose_name='Время прибытия')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена билета')

    def __str__(self):
        return f'{self.bus} - {self.route} - {self.departure_time} - {self.arrival_time}'

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'


class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='Рейс')
    purchase_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')

    def __str__(self):
        return f'{self.user} - {self.trip}'

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
