from django.db.models import fields
from rest_framework import serializers
from .models import User, Review, CourseHeader
from .documents import CourseHeaderDocument

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from api import documents

from api import models


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

class UserSerializer(serializers.ModelSerializer):
    time_onscreen_page = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='keyword'
     )
    most_action_each_page =  serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='keyword'
    )
    most_url_click =  serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='keyword'
    )
    class Meta:
        model = User
        fields = ('userid','name', 'avatar','type1','type2','type3','time_onscreen_page','most_action_each_page','most_url_click')

class CourseForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseHeader
        fields = ['course_title','course_tag','course_image','about','rating_count','rating','enrolled','keyword','language', 'offer_by','subtitle', 'course_url']

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