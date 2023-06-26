from django.db import models
from django.forms import ValidationError
from django.utils import timezone

class Owner(models.Model):
    name = models.CharField(max_length=100)
    # Другие поля для владельца

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

class Field(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # Другие поля для поля

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'


class Booking(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    selected_date = models.DateField()
    selected_start_time = models.TimeField(verbose_name='Начальное время', default=timezone.now)
    selected_end_time = models.TimeField(verbose_name='Конечное время', default=timezone.now)
    # Другие поля для бронирования
    def clean(self):
        # Проверка, что конечное время больше начального времени
        if self.selected_start_time and self.selected_end_time:
            if self.selected_start_time >= self.selected_end_time:
                raise ValidationError("Конечное время должно быть больше начального времени")
    
    class Meta():
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

