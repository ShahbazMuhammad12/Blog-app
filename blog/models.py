from django.db import models
import datetime

class Blog(models.Model):
    title = models.CharField(max_length=20)
    created_date = models.DateField(auto_now=False,auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text
