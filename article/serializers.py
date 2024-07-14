from rest_framework import serializers
from .models import Article, CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        password = attrs.get('password')
        if not password.isalnum():
            raise serializers.ValidationError('Password field must be contain alpha symbol and numbers!')
        if len(attrs.get('password')) < 8:
            raise serializers.ValidationError('password do not match')
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            **validated_data
        )
        return user


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'description', 'is_public')
        read_only_fields = ('author',)