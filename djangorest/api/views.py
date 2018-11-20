from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import BucketlistSerializer
from .models import Bucketlist

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """Only return bucketlist items owned by the currently authenticated user."""
        user = self.request.user
        return Bucketlist.objects.filter(owner=user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
