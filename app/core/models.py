from django.db import models

class Todo(models.Model):
    user_id = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    title = models.CharField(max_length=25)
    text = models.TextField(max_length=100, blank=True, null= True)
    date = models.CharField(max_length=25, default="")
