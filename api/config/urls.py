from django.urls import path
from django.urls import include

urlpatterns = [
    path('api/books/', include('apps.books.urls', namespace='books')),
    path('api/auth/', include('apps.auth.urls', namespace='auth')),
    path('api/captcha/', include('apps.captcha.urls')),
]
