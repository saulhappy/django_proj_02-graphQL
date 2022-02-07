from django.db import models

class Books(models.Models):
    title=models.CharField(max_length=140)
    excerpt=models.TextField()

    def __str__(self):
        return self.title