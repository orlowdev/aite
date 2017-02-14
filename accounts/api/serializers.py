from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    EmailField,
)


User = get_user_model()


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email"
        ]


class UserCreateSerializer(ModelSerializer):
    email = EmailField()

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


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]

        # Set password to be hidden upon user creation
        extra_kwargs = {"password": {
            "write_only": True}
        }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("Email or username is required")

        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Invalid email or username")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Provided credentials do not match")

        data["token"] = "TOKEN"

        return data
