from django.db import models
from trainee.models import Trainee
from trainer.models import Trainer
from facility.models import Facility
from sports_gear.models import SportsGear
# Create your models here.

class Training(models.Model):
    TRAINING_TYPE_CHOICES = (
        ("expert", "expert"),
        ("beginner", "beginner"),
        ("intermediate", "intermediate")
    )
    TRAINING_LEVEL_CHOICES = (
        ("Tactic training", "Tactic training"),
        ("Psychological training", "Psychological training"),
        ("Strength and conditional workout", "Strength and conditional workout"),
        ("Strength and conditioning workouts", "Strength and conditioning workouts"),
        ("Developing positivity when approaching a contest", "Developing positivity when approaching a contest"),
    )

    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE, null=False)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=False)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True)
    sportsgear = models.ForeignKey(SportsGear, on_delete=models.CASCADE, null=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False,null=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False,null=False)
    training_date = models.DateField(auto_now_add=False, auto_now=False, null=False)
    training = models.CharField(max_length=255, null=True)
    training_type = models.CharField(max_length=30, choices=TRAINING_TYPE_CHOICES, null=False)
    training_level = models.CharField(max_length=225, choices=TRAINING_LEVEL_CHOICES, null=True)

    def __str__(self):
        training = f"{self.trainer} -  trained  {self.trainee},  on  {self.training_date} from {self.start_time} to {self.end_time}"
        return training