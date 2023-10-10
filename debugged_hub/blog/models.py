from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

"""Create an auth token for a newly created user."""
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    # Check if the user is newly created
    if created:
        # Create and save new token
        Token.objects.create(user=instance)

# UserProfile model
class UserProfile(models.Model):
    # OneToOneField: One user has one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=False, blank=True)
    email = models.EmailField(null=False, unique=True, blank=True)
    password = models.CharField(max_length=255, null=False, blank=True)
    first_name = models.CharField(max_length=255, null=False, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=True)
    
    # BooleanField: Is the user a writer?
    is_writer = models.BooleanField(default=False)

    # Add other fields like profile picture, bio, etc. as needed

    def __str__(self):
        # Return the username of the user
        return self.user.username

# Admin model
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=True)
    email = models.EmailField(null=False, unique=True, blank=True)
    password = models.CharField(max_length=255, null=False, blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.user.username


# Topics Model
class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # Add other fields like description, parent topic (if you want to create a hierarchy), etc.

    def __str__(self):
        return self.name

# Blog model
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    topics = models.ManyToManyField(Topic)  # Many-to-Many relationship with Topic
    # Add other fields like tags, categories, etc. as needed

    def __str__(self):
        return self.title

# writer model
class Writer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Add other fields like specialization, experience, etc. as needed

    def __str__(self):
        return self.user.user.username


