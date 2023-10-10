from rest_framework import serializers
from .models import Blog, Topic, UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer()

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def create(self, validate_data):
        user = self.context['request'].user
        if user.is_superuser or user.is_staff or user.is_verified_writer:
            blog = Blog.objects.create(**validated_data, author=user)
            return blog
        raise serializers.ValidationError('Unauthorized Access!')

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.is_superuser or user.is_staff or (user.is_verified_writer and instance.author == user):
            instance.title = validated_data.get('content', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.topic = validated_data.get('topic', instance.topic)
            instance.save()
        raise serializers.ValidationError("Unauthorized Access")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True}
        }

    def validate_email(self, value):
        # Validate email format
        if not value:
            raise serializers.ValidationError("Email is Required.")
        return value

    def validate(self, data):
        # Ensure required fields are provided before creating the user
        if not data.get('email') or not data.get('first_name') or not data.get('last_name'):
            raise serializers.ValidationError("Email, first name, and last name are required fields.")
        return data

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
            return user
        except IntegrityError:
            raise serializers.ValidationError("This email is already in use.")

    def update(self, instance, validated_data):
        # ensure required fields are provided before updating the user

        password = validated_data.pop('password', None)
        instance = super(UserSerializer, self).update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance

