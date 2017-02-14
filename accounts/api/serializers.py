from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    CharField
)


User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

        # Set password to be hidden upon user creation
        extra_kwargs = {"password": {
            "write_only": True}
        }

    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This email is already taken.")

        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            username=username,
            email=email,
        )

        user_obj.set_password(password)
        user_obj.save()

        return validated_data
