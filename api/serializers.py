from rest_framework import serializers
from .models import User, Review, CourseHeader
from .documents import CourseHeaderDocument

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from api import documents

from api import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userid','email','name','password', 'avatar','provider')

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'password')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email', 'password')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('reviewer','review_text', 'star', 'review_vote', 'review_date')


class CourseSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
   
    class Meta:
        model = CourseHeader
        fields = ['course_title','course_tag','course_image','about','rating_count','rating','enrolled','keyword','review','language', 'offer_by','subtitle', 'course_url']


class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseHeader
        fields = ('star', 'review_text')

class CreateRelatedCourse(serializers.ModelSerializer):
    class Meta:
        model = CourseHeader
        fields = ['course_title', 'course_image','course_url','about','rating_count','offer_by']

class CourseHeaderDocumentSerializer(DocumentSerializer):
    class Meta:
        document = CourseHeaderDocument
        fields = [
            'about',
        ]
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('username','password')