from rest_framework import serializers
from users.models import UserProfile, User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'bloodCenter',
        )


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'password', 'profile', 'mobile')
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

        profile.bloodCenter = profile_data.get('bloodCenter', profile.bloodCenter)
        profile.save()

        return instance
