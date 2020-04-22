from rest_framework import serializers
from api.models import BloodCenter, Donor, History, GetName


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
            'name',
            'gender',
            'phone_num',
            'age',
            'blood_type',
            'admin_id',
        ]


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = [
            'date',
            'blood_center_id',
        ]


class GetNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetName
        fields = [
            'date',
            'name',
        ]
