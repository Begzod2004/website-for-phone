from distutils.command.upload import upload
from django.db import models




class Brand(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f"{self.name}"


class Company(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f"{self.title}"

    

class Fps(models.Model):
    fps = models.IntegerField()
    def __str__(self) -> str:
         return f"{self.fps}"

class sistem(models.Model):
    name = models.CharField(max_length=30)
    

class Phone(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.FloatField()
    abaut = models.CharField(max_length=500)
    img = models.ImageField(upload_to= 'static/images')
    memory = models.IntegerField()
    fps = models.ForeignKey(Fps, on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    sistem = models.ForeignKey(sistem,on_delete=models.CASCADE)
    def save(self):
        return super().save()

    def __str__(self) -> str:
        return f"{self.name} {self.company} {self.price} {self.brand} {self.img} {self.memory} {self.fps} {self.color}"
    