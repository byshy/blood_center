from rest_framework import serializers
from api.models import User, UserProfile, BloodCenter, Donor, History, GetName


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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'mobile',
            'bloodCenter',
        )


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        """By using set_password, the password is hashed and stored as a hash rather than plaintext which is a very 
        important point in terms of security. """
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.mobile = profile_data.get('mobile', profile.mobile)
        profile.bloodCenter = profile_data.get('bloodCenter', profile.bloodCenter)
        profile.save()

        return instance
