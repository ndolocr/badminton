from django.db import models

# Create your models here.

class Equipment(models.Model):
    name = models.CharField(max_length=255, null=False)
    equipment_type = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name