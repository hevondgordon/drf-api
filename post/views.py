from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
