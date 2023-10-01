from rest_framework import serializers
from .models import Blog, Topic, UserProfile

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
        if user.is_staff or user.is_verified_writer:
            blog = Blog.objets.create(**validated_data, auther=user)
            return blog
        raise serializers.ValidationError('Unauthorized Access!')

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.is_staff or (user.is_verified_writer and instance.author == user):
            instance.title = validated_data.get('content', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.topic = validated_data.get('topic', instance.topic)
            instance.save()
        raise serializers.ValidationError("Unauthorized Access")