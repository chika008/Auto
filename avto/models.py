
from django.db import models

# Create your models here.

class Auto(models.Model):
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    title = models.CharField(verbose_name='Название автомобиля',max_length=100)
    image = models.ImageField(verbose_name='Изображение автомобиля',upload_to='images/',blank=True, null=True)
    car_body = models.ForeignKey(
        'avto.Body', on_delete=models.PROTECT, related_name='Body', verbose_name='Кузов автомобиля')
    price = models.DecimalField(verbose_name="цена",max_digits=10, decimal_places=2)
    year = models.CharField(verbose_name='Год выпуска',max_length=4)
    color = models.ForeignKey(
        'avto.Color', on_delete=models.PROTECT, related_name='Color', verbose_name='цвет автомобиля')
    description = models.TextField(verbose_name='описание')
    is_published = models.BooleanField(verbose_name='публичность', default=True)
    date = models.DateTimeField(verbose_name='дата добавление',auto_created=True)

   


    def __str__(self):
        return f'{self.title}'
    
class Color(models.Model):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        
    name = models.CharField(verbose_name='цвет автомобиля', max_length=100)
    def __str__(self):
        return f'{self.name}'
    

class Body(models.Model):
    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузова'
    
    name = models.CharField(verbose_name='Кузов автомобиля',max_length=50)
    def __str__(self):
        return f'{self.name}'

