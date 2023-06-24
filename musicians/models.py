from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=30)
    INSTRUMENT = (
        ('g', 'Гитара'),
        ('v', 'Скрипка'),
        ('p', "Пианино"), 
        ('d', 'Барабан')
    )

    instrument = models.CharField(max_length=30, choices=INSTRUMENT)
    progress = models.IntegerField()
    payment = models.CharField(max_length=30)


    def __str__(self) -> str:
        return f'{self.name} - {self.surname} - {self.pk}'
    

    def get_absolute_url(self):
        return f"/{self.pk}"