from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import User

@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Site'
        message = f'Hi {instance.username}, thank you for registering at our site.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [instance.email]

        send_mail(subject, message, from_email, recipient_list)
