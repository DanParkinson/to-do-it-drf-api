from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    '''
    Categories model, linked to 'owner' User.
    Each user can create their own categories.
    '''
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name} (by {self.owner.username})'