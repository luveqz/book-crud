from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import password_validation as validators
from django.utils import timezone

from rest_framework import serializers
from captcha.models import CaptchaStore

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    captcha_key = serializers.CharField(write_only=True)
    captcha = serializers.CharField(write_only=True)

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('email', 'username', 'name', 'password',
                  'password2', 'captcha_key', 'captcha')

    def validate_password(self, password):
        data = self.context['request'].data
        username = data.get('username', '')

        user = User(username=username)
        validators.validate_password(password, user)

        if password != data.get('password2', ''):
            raise serializers.ValidationError(
                _("The two password fields didn't match."))

        return password

    def validate_captcha(self, captcha):
        data = self.context['request'].data
        captcha_key = data.get('captcha_key', '')

        try:
            CaptchaStore.objects.get(
                response=captcha,
                hashkey=captcha_key,
                expiration__gt=timezone.now()
            ).delete()

        except CaptchaStore.DoesNotExist:
            raise serializers.ValidationError(
                _("Invalid CAPTCHA"))

        return captcha

    def clean_data(self, data):
        data.pop('password2')
        data.pop('captcha_key')
        data.pop('captcha')

    def create(self, validated_data):
        self.clean_data(validated_data)
        return User.objects.create_user(**validated_data)
