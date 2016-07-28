# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tag, Book, Library

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'name')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'tags', 'name', 'authorFName', 'authorLName', 
            'insertedDate', 'publishedYear', 'firstPublishedYear', 'pages')


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ('url', 'user', 'book', 'avah', 'ogoh')