from django.urls import path
from .views import *

urlpatterns = [
    # Users
    path('users/',UsersView.as_view()),
    path('users/post/',UsersCreate.as_view()),
    path('users/<int:pk>',UsersUpdate.as_view()),
]