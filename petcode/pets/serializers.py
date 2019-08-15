from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from petcode.pets.models import Pet, PetType, Size, Gender, CategoryStatus, Category 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class PetTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PetType
        fields = ['url', 'name']


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ['url', 'name']

class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = ['url', 'name']

class CategoryStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryStatus
        fields = ['url', 'name', 'category']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name']

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = [
            'url', 
            'user', 
            'image', 
            'name', 
            'description', 
            'pet_type', 
            'size', 
            'gender', 
            'category', 
            'state', 
            'city', 
            'contact_name',
            'phone_1',
            'phone_2',
            'email',
            'published_date'
        ]

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
        max_length=32,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        