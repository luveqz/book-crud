from rest_framework.decorators import api_view
from rest_framework.response import Response
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from captcha.helpers import captcha_audio_url


@api_view(['GET'])
def captcha_refresh(request):
    new_key = CaptchaStore.pick()

    return Response({
        "key": new_key,
        "image_url": captcha_image_url(new_key),
        "audio_url": captcha_audio_url(new_key)
    })
