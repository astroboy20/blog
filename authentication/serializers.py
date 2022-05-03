import email
from .models import User

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['email', 'username', 'firstname',
                  'lastname', 'phone_number', 'password']

    def validate(self, attrs):
        # username_exists = User.objects.filter(
        #     username=attrs['username']).exists()
        # if username_exists:
        #     raise serializers.ValidationError(
        #         detail="User with this username already exists")

        # email_exists = User.objects.filter(
        #     email=attrs['email']).exists()
        # if email_exists:
        #     raise serializers.ValidationError(
        #         detail="User with this email already exists")

        phone_number_exists = User.objects.filter(
            phone_number=attrs['phone_number']).exists()
        if phone_number_exists:
            raise serializers.ValidationError(
                detail="User with this phone number already exists")

        return super().validate(attrs)
