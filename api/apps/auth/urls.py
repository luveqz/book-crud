from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = 'auth'

urlpatterns = [
    path('get-token', obtain_auth_token, name='get-token'),
    path('signup', views.SignUpView.as_view(), name='signup'),
]
