from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Category


@receiver(post_save, sender=User)
def create_uncategorized_category(sender, instance, created, **kwargs):
    """
    Automatically creates an 'Uncategorized' category for new users.
    """
    if created:
        Category.objects.create(owner=instance, name="Uncategorized")