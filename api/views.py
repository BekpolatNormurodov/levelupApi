from .models import Users
from .serializers import UsersSerializer
from rest_framework.generics import *

# USERS
class UsersView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersCreate(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer