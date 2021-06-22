from re import split
from django.db.models import query
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import generics, status, permissions
from .serializers import CreateUserSerializer, CourseForUserSerializer, UserSerializer, LocalSerializer, CourseSerializer, CreateCourseSerializer, ReviewSerializer, CreateRelatedCourse, LoginSerializer,UserActionTimeSerializer,UserActionClickSerializer
from .models import User,CourseHeader, Review,UserActionTime
from rest_framework.views import APIView
from rest_framework.response import Response

from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
from . import serializers
from . import models

import elasticsearch
import logging
from .documents import CourseHeaderDocument

from .utils import is_empty_or_null, rebuild_elasticsearch_index, delete_elasticsearch_index

import string
import random

from django.db import connection
# Create your views here.
class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        userName = self.request.query_params.get('username')
        if userName is not None: # not input param, just show all course to view.
            queryset = queryset.filter(username=userName) #just get detail of course filter by course_tag.
        return queryset

class CourseForUser(generics.ListAPIView):
    serializer_class = CourseForUserSerializer
    def get_queryset(self):
        queryset = None
        key_courses_1 = self.request.query_params.get('k1')
        key_courses_2 = self.request.query_params.get('k2')
        q_1 = list(CourseHeader.objects.filter(keyword=key_courses_1).order_by('-score'))
        q_2 = list(CourseHeader.objects.filter(keyword=key_courses_2).order_by('-score'))
    
        if(key_courses_1 == key_courses_2):
            queryset = random.choices(q_1 , k=50)
        elif(key_courses_1 != key_courses_2):
            queryset = random.choices(q_1 + q_2 , k=50)
        return queryset

class CourseView(generics.ListAPIView):
    serializer_class = CourseSerializer
    def get_queryset(self):
        queryset = CourseHeader.objects.order_by('-rating_count')
        courseTag = self.request.query_params.get('course_tag')
        nonReview = self.request.query_params.get('review_option')
        if courseTag is not None: # not input param, just show all course to view.
            queryset = queryset.filter(course_tag=courseTag) #just get detail of course filter by course_tag.
        elif nonReview is not None:
            queryset = CourseHeader.objects.values()
        return queryset
class Login(generics.ListAPIView):
    serializer_class = LoginSerializer

    def get_queryset(self):

        username = self.request.query_params.get('username')
        password = self.request.query_params.get('password')
      
        queryset = User.objects.filter(username=username).filter(password=password)
        
        if queryset is not None:
            return status.HTTP_200_OK
        else:
            return status.HTTP_400_BAD_REQUEST
            

class RelatedCourse(generics.ListAPIView):
    serializer_class = CourseSerializer


    def get_queryset(self):

        keyword = self.request.query_params.get('keyword')
        print(keyword)
        queryset = CourseHeader.objects.filter(keyword=keyword).order_by('-score')
        return queryset

class CreateCourse(APIView):
    serializer_class = CreateCourseSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            star = serializer.data.get('star')
            review_text = serializer.data.get('review_text')
            course = Course.objects.create(star = star, review_text = review_text)

            return Response(CreateCourseSerializer(course).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    
class CreateUser(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        queryset = User.objects.filter(email=serializer.initial_data['email'])
        if(len(queryset) > 0):
            return Response("Email exists", status=status.HTTP_200_OK)
        elif serializer.is_valid():
            name = serializer.data.get('name')
            # username = serializer.data.get('username')
            email = serializer.data.get('email')
            password = serializer.data.get('password') 
            user = User.objects.create(userid=generate_unique_code(), name=name, username = email.split('@')[0], email=email, password = password)

            return Response(CreateUserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)



def generate_unique_code():
    length = 9

    while True:
        code = ''.join(random.choices(string.ascii_letters, k=length))
        if User.objects.filter(userid=code).count() == 0:
            break
    return code


class LocalLoginView(APIView):
    serializer_class = LocalSerializer
   
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)    
        print(serializer)  
        if serializer.is_valid():
            email = serializer.data.get('email')
            name = serializer.data.get('name')
            password = serializer.data.get('password')
            queryset = User.objects.filter(email=email)
            if len(queryset) > 0:
                return Response("Email exists", status=status.HTTP_200_OK)
            else:
                user = User.objects.create(userid=generate_unique_code(), email=email,
                            name=name, password=password)
                user.save()
                
                return Response(LocalSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class GetUserAction(APIView):
    def post(self, request, format=None):
        userid = request.data.get('userid', None)
        list_action_time = request.data.get('list_action_time', None)
        list_action_click = request.data.get('list_action_click',None)
        if userid!=None:
            cur = connection.cursor()
            if list_action_time != None:
                print (list_action_time)
                for i in list_action_time:
                    cur.callproc("AddCount_UserActionTime", [userid, i['page'],i['time_onscreen']])
                
            if  list_action_click != None:
                for i in list_action_time:
                    cur.callproc("AddCount_UserActionClick", [userid, i['page'],i['click_count']])
            cur.close()
            return Response({'Success': 'J Hello'}, status=status.HTTP_201_CREATED)
           
"""
View file
"""




class CourseSearchView(APIView):

    """
    format the response with message, status, data
    and send as api response
    """
    def __send_response(self, message,word_search,suggest_word, score,status_code,data=None):
        content = {
            "message": message,
            "word_search": word_search,
            "suggest_word":suggest_word,
            "score": score,
            "result": data if data is not None else []
            }
        return Response(content, status=status_code)

    """
    handle post request
    filter the sammmaries data based on given query list with k number 
    """
  
    def post(self, request):
        filter1 = ''
        query_list = request.data.get('queries', None)
        filter1 = request.data.get('filter', None)
     
        flag = request.data.get('flag', None)
       
        k = 50# k = query_list.count()
        # response = None

        if is_empty_or_null(query_list):
            error_message = "queries should not be empty"
            return self.__send_response(error_message, status.HTTP_400_BAD_REQUEST)
        # if type(query_list) != list:
        #     error_message = "queries should be list of query/keywords"
        #     return self.__send_response(error_message, status.HTTP_400_BAD_REQUEST)

        if is_empty_or_null(k):
            error_message = "k should be integer and not empty"
            return self.__send_response(error_message, status.HTTP_400_BAD_REQUEST)

        try:
            #rebuild_elasticsearch_index()
            es = elasticsearch.Elasticsearch()
            if (es.indices.exists("courseheader_data")!=True):
                # build elastic search index
                rebuild_elasticsearch_index()
            score = 0
            suggest_word=''
            if int(flag)==0:
                results =es.search(
                index="courseheader_data",
                doc_type="_doc",
                body={
                     "suggest": {
                     "full-suggestion": {
                     "prefix" : query_list, 
                         "completion" : { 
                          "field" : "course_title.suggest",
                
                             "size": 50
                        }}}})
                response = {'courses': results['suggest']['full-suggestion'][0]['options']}

            else:
                _len = len(str(query_list).split(' '))
                results_suggest = es.search(
                            index = "courseheader_data", 
                            doc_type = "_doc", 
                            body = {
                                    "suggest" : {
                                        "suggestion1" : {
                                            "text" : query_list,
                                            "term" : {
                                                    "field" : "about"
                                                    }
                                                        }   
                                                }
                                    })   
                for i in range(0,_len):
                    if (len(results_suggest['suggest']['suggestion1'][i]['options'])==0):
                        suggest_word+= results_suggest['suggest']['suggestion1'][i]['text']+ ' '
                        score+=1
                    else:
                        suggest_word+= results_suggest['suggest']['suggestion1'][i]['options'][0]['text'] +' '
                        score+=results_suggest['suggest']['suggestion1'][i]['options'][0]['score']
                score /= _len  
                if (filter1 == None) or filter1== '':
                    results =es.search(
                    index="courseheader_data",
                    doc_type="_doc",
                    body={
                        "query": {"multi_match": {
                        "query": query_list,
                        "fields": ["about","course_title","skill_gain"],"fuzziness":"AUTO"
        
                                                    }
                                    },"size":50
                            })
                else:
                    filterquery =[]
                    filterquery.append({"multi_match":{"query":query_list,"fields": ["about","course_title","skill_gain"],"fuzziness":"AUTO"}})
                    for language in str(filter1).split(','):
                        filterquery.append( {"match":{"subtitle":language}})
                    results =es.search(
                    index="courseheader_data",
                    doc_type="_doc",
                    body={
                        "query": {"bool": {"must": filterquery
                        }
                                },"size": 50
                            })
                response = {'courses': results['hits']['hits']}
           
            # delete elastic search index
            #delete_elasticsearch_index()
        except elasticsearch.ConnectionError as connection_error:

            error_message = "Elastic search Connection refused"
            return self.__send_response(error_message, status.HTTP_503_SERVICE_UNAVAILABLE)

        except Exception as exception_msg:
           
            error_message = str(exception_msg)
            return self.__send_response(error_message, status.HTTP_400_BAD_REQUEST)

        return self.__send_response('success',query_list,suggest_word,score, status.HTTP_200_OK, response)