from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=99)

    def __str__(self):
        return self.name

    def summary(self):
        show = []
        show = self.description.split()
        res = ""
        for i in range(25):
            res += show[i] + " "
        return res
