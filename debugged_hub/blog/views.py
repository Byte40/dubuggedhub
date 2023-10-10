from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Blog, UserProfile
from .serializers import BlogSerializer, UserSerializer
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class CreateBlogAPIView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the author field to the authenticated user making the request
        serializer.save(author=self.request.user)


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        user = self.request.user
        if user.is_superuser or user.is_staff or (user.is_verified_writer and serializer.instance.author == user):
            serializer.save()
        else:
            raise serializers.ValidationError("Unauthorized Access")

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'id': user.id, 'token': token.key})
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = User.get_object()
        password = request.data.get('password', None)
        if not password or not user.check_password(password):
            return Response({'error': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
        return super(UserDetailAPIView, self).update(request, *args, **kwargs)

    for user in User.objects.all():
        Token.objects.get_or_create(user=user)

class UserLoginAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class =  UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            return Response({'id': user.id, 'token': user.auth_token.key})
        else:
            return Response ({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserAccountDeletionRequestAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        if user != request.user:
            return Response({'error': 'Unauthorized Request'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'Request Successfull!'}, status=status.HTTP_200_OK)

