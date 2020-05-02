from rest_framework import serializers
from api.models import BloodCenter, Donor, History


class BloodCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodCenter
        fields = [
            'longitude',
            'latitude',
            'name',
        ]


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = [
            'id',
            'gender',
            'age',
            'blood_type',
        ]


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = [
            'date',
            'blood_center_id',
        ]
