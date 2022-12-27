from django.db import models

# Create your models here.

class Trainer(models.Model):
    TRAINER_LEVEL_CHOICES = (
        ("expert", "expert"),
        ("beginner", "beginner"),
        ("intermediate", "intermediate")
    )
    name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=20, null=True)
    trailer_level = models.CharField(max_length=30, choices=TRAINER_LEVEL_CHOICES, null=False)

    def __str__(self):
        return self.name
    
