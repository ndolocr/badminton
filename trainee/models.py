from django.db import models

# Create your models here.

class Trainee(models.Model):
    TRAINEE_LEVEL_CHOICES = (
        ("expert", "expert"),
        ("beginner", "beginner"),
        ("intermediate", "intermediate")
    )

    GENDER_CHOICES = (
        ("male", "male"),
        ("female", "female"),
        ("other", "other")
    )

    name = models.CharField(max_length=255, null=True)
    dob = models.DateField(auto_now=False, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    trailer_level = models.CharField(max_length=30, choices=TRAINEE_LEVEL_CHOICES, null=False)

    def __str__(self):
        return self.name
    
