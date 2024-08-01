from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Teacher

@receiver(post_save, sender=Teacher)
def teacher_created(sender, instance, created, **kwargs):
    if created:
        print(f"New teacher created: {instance.full_name}")

