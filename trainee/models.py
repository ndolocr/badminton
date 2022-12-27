from django.db import models

# Create your models here.

class Trainee(models.Model):
    TRAINEE_LEVEL_CHOICES = (
        ("expert", "expert"),
        ("beginner", "beginner"),
        ("intermediate", "intermediate")
    )
    name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=20, null=True)
    dob = models.DateField(auto_now=False, null=True)
    trailer_level = models.CharField(max_length=30, choices=TRAINEE_LEVEL_CHOICES, null=False)

    def __str__(self):
        return self.name
    
