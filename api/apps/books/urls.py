from django.urls import path
from apps.books import views

app_name = 'books'

urlpatterns = [
    path('', views.BookList.as_view()),
    path('<int:pk>/', views.BookDetail.as_view()),
]
