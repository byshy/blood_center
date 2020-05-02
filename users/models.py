from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.CharField(max_length=9, primary_key=True)
    username = models.CharField(blank=True, null=True, max_length=30)
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=13)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id', 'username', 'first_name', 'last_name', 'mobile']

    def __str__(self):
        return "{}, {} {}".format(self.id, self.first_name, self.last_name)


class WorksAt(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    bloodCenter = models.ForeignKey('api.BloodCenter', on_delete=models.DO_NOTHING, null=True, blank=True)
