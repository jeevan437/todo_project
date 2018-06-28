from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('PARKED', 'Parked'),
    ('STARTED', 'Started'),
    ('FINISHED','Finished')
)
class todo_model(models.Model):

    task_name = models.CharField(max_length=100, unique=True)
    task_description =models.TextField()
    task_status = models.CharField(max_length=100,choices=STATUS_CHOICES)

    def __str__(self):
        return self.task_name