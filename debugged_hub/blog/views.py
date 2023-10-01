from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializer

class BlogListAPIView(generics.ListAPIView):
    # Get all blogs
    queryset = Blog.objects.all()
    # Serialize the blogs
    serializer_class = BlogSerializer

class BlogDetailAPIView(generics.RetrieveAPIView):
    # Retrieve a single blog by id
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'

# Get blogs by associated id
class BlogByTopicAPIView(generics.ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        return Blog.objects.filter(topic__id=topic_id)

# Get blogs by associated auther
class BlogByWriterAPIView(generics.ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        writer_id = self.kwargs['writer_id']
        return Blog.objects.filter(author__id=writer_id)

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'
    permission_classes = [permiossions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Blog.objets.all()
        elif user.is_verified_writer:
            return Blog.objects.filter(auther=user)
        else:
            return Blog.objects.none()

    def perform_create(self, serializer):
        serializer.save(auther=self.request.user)
