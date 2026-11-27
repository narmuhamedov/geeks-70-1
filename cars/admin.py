from django.contrib import admin
from cars.models import CategoryCar, Car, StateNumberCar,CommentCar

admin.site.register(CategoryCar)
admin.site.register(Car)
admin.site.register(StateNumberCar)
admin.site.register(CommentCar)