from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Blog

@receiver(pre_save, sender=Blog)
def set_blog_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

        if Blog.objects.filter(slug=instance.slug).exists():
            i = 1
            while True:
                new_slug = f"{instance.slug}-{i}"
                if not Blog.objects.filter(slug=new_slug).exists():
                    instance.slug = new_slug
                    break
                i += 1
