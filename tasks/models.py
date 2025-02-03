from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    '''
    Task model, related to 'owner', i.e a User interface
    '''
    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
        ('Overdue','Overdue'),
    ]

    PRIORITY_CHOICES = [
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending',
    )
    priority = models.CharField(
        max_length=20,
        choices = PRIORITY_CHOICES,
        default = 'Medium',
    )
    # category
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.owner} - {self.title} - id = {self.id}'

