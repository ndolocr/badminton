from django.db import models
from trainee.models import Trainee
from trainer.models import Trainer
# Create your models here.

class Training(models.Model):
    TRAINING_TYPE_CHOICES = (
        ("expert", "expert"),
        ("beginner", "beginner"),
        ("intermediate", "intermediate")
    )
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE, null=False)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False,null=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False,null=False)
    training_date = models.DateField(auto_now_add=False, auto_now=False, null=False)
    training_type = models.CharField(max_length=30, choices=TRAINING_TYPE_CHOICES, null=False)

    def __str__(self):
        training = self.trainer + " trained " + self.trainee + " on " + self.training_date
        return training