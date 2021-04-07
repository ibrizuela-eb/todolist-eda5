from django.db import models
from django.conf import settings 

# Create your models here.
class Priority(models.Model):
    order = models.IntegerField()
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class Todo(models.Model):
    description = models.CharField(max_length=30)
    done = models.BooleanField(default=False)
    priority = models.ForeignKey(
        Priority, 
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    user_assigned = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        default=None,
        null=True,
        )

    def __str__(self):
        return self.description
