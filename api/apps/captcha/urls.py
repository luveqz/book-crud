from django.urls import include, path, re_path
from captcha.views import captcha_image
from captcha.views import captcha_audio

from . import views

urlpatterns = [
    re_path(
        r"image/(?P<key>\w+)/$",
        captcha_image,
        name="captcha-image",
        kwargs={"scale": 1},
    ),
    re_path(
        r"image/(?P<key>\w+)@2/$",
        captcha_image,
        name="captcha-image-2x",
        kwargs={"scale": 2},
    ),
    re_path(
        r"audio/(?P<key>\w+).wav$",
        captcha_audio,
        name="captcha-audio"
    ),
    path('refresh', views.captcha_refresh, name='captcha-refresh'),
]
