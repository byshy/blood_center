from django.db import models
from django.utils import timezone
from users.models import User


class Donor(models.Model):
    GENDERS_LIST = (
        (1, 'male'),
        (2, 'female'),
        (3, 'other'),
    )

    BLOOD_TYPE_LIST = (
        (1, 'A+'),
        (2, 'A-'),
        (3, 'B+'),
        (4, 'B-'),
        (5, 'O+'),
        (6, 'O-'),
        (7, 'AB+'),
        (8, 'AB-'),
    )

    id = models.OneToOneField(User, on_delete=models.DO_NOTHING, primary_key=True)
    gender = models.PositiveSmallIntegerField(choices=GENDERS_LIST)
    age = models.IntegerField()
    blood_type = models.PositiveSmallIntegerField(choices=BLOOD_TYPE_LIST)

    def __str__(self):
        return "{}".format(self.id)


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
