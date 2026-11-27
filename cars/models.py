from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#MANY TO MANY
class CategoryCar(models.Model):
    name = models.CharField(max_length=100, default="#")

    def __str__(self):
        return self.name

class Car(models.Model):
    title = models.CharField(max_length=100)
    vin_code = models.CharField(max_length=100)
    person = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    #Тут связыываем таблицу Car с CategoryCar в отношении многие ко многим
    categories = models.ManyToManyField(CategoryCar, blank=True, null=True)

    def __str__(self):
        return f'{self.title}-{self.person}'


#ONE TO ONE
class StateNumberCar(models.Model):
    car_choice = models.OneToOneField(Car, on_delete=models.CASCADE)
    number_car = models.CharField(max_length=100, default='0_KG______')

    def __str__(self):
        return f'{self.car_choice}-{self.number_car}'


#One TO Many
class CommentCar(models.Model):
    car_choice = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, related_name='reviews')
    description = models.TextField(blank=True)
    mark = models.FloatField(default=5.0, validators=[MinValueValidator(1.0), 
                                                      MaxValueValidator(10.0)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car_choice}-{self.mark}'
