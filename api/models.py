from django.db import models
from django.utils import timezone
from users.models import User


class Donor(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1)
    phone_num = models.CharField(max_length=13)
    age = models.IntegerField()
    blood_type = models.CharField(max_length=3)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{} {}".format(self.id, self.name)


class BloodCenter(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return "{}".format(self.name)


class History(models.Model):
    date = models.DateTimeField('date-time created', default=timezone.now)
    user_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    blood_center_id = models.ForeignKey(BloodCenter, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{} {}".format(self.date, self.user_id)

    class Meta:
        unique_together = (("date", "user_id"),)
