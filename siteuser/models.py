from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
# Create your models here.


def upload_to(instance, filename):
    return 'user_profile_pics/%s/%s' % (instance.user.id, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to=upload_to)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.user.username

    