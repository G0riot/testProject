from django.db import models


# Create your models here.
class Questionary(models.Model):
    text = models.CharField(max_length=1000, default='')
    use = models.BooleanField(default=True)

    def __str__(self):
        return self.text
