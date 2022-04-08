from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from snippets.models import Snippet,Register


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ("username", "email", "password")

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields =  "__all__"
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ["username","password"]
