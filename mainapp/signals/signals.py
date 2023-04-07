import os
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from mainapp.models import Avatar



@receiver(post_save, sender=User)
def create_default_avatar(sender, instance, created, **kwargs):
    if created:
        default_avatar_path = os.path.join(settings.MEDIA_ROOT, 'default_avatar.png')

        if os.path.exists(default_avatar_path):
            with open(default_avatar_path, 'rb') as f:
                avatar = Avatar(user=instance, imagen=f)
                avatar.save()

post_save.connect(create_default_avatar, sender=User)