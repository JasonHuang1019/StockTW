# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 11:04:22 2021

@author: Huang
"""

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES,Stock


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields =['status']
#%%
from django.contrib.auth.models import User, Group
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')