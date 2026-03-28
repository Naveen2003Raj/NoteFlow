from django.db import models
from django.contrib.auth.models import User

class StickyNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"


class Todo(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task