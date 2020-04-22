from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=30)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class Donor(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1)
    phone_num = models.CharField(max_length=13)
    age = models.IntegerField()
    blood_type = models.CharField(max_length=3)
    admin_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{} {}".format(self.id, self.name)


class BloodCenter(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return "{}".format(self.name)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    mobile = models.CharField(max_length=13)
    bloodCenter = models.ForeignKey(BloodCenter, on_delete=models.DO_NOTHING)


class History(models.Model):
    date = models.DateTimeField('date-time created')
    user_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    blood_center_id = models.ForeignKey(BloodCenter, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{} {}".format(self.date, self.user_id)

    class Meta:
        unique_together = (("date", "user_id"),)


class GetName(models.Model):
    name = models.ForeignKey(BloodCenter, on_delete=models.DO_NOTHING)
    date = models.ForeignKey(History, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (("date", "name"),)
