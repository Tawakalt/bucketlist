from rest_framework import generics, permissions
from .permissions import IsOwnerOrAdmin
from .serializers import BucketlistSerializer, UserSerializer, CategorySerializer
from .models import Bucketlist, User, Category
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.response import Response

# Create your views here.

class CreateBucketlist(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

    @method_decorator(cache_page(60*15))
    def get(self, request):
        """Only return bucketlist items owned by the currently authenticated user."""
        user = self.request.user
        queryset = self.get_queryset() if user.is_superuser else Bucketlist.objects.filter(owner=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BucketListDetails(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)


class UserManager(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
        

class CreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def perform_create(self, serializer):
        serializer.save()

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


