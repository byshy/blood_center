from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=30)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    mobile = models.CharField(max_length=13)
    bloodCenter = models.ForeignKey('api.BloodCenter', on_delete=models.DO_NOTHING)