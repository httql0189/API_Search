from django.db import models
from django.utils import timezone
# Create your models here.
import string
import random

def generate_unique_id():
    length = 8

    while True:
        code = ''.join(random.choices(string.ascii_letters, k=length))
        if CourseHeader.objects.filter(course_id=code).count() == 0:
            break
    return code



class CourseHeader(models.Model):
    course_url = models.CharField(max_length=100)
    course_tag = models.CharField(primary_key=True,max_length=100)
    course_title = models.CharField(max_length=100, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    rating_count = models.CharField(max_length=20, blank=True, null=True)
    review_count = models.CharField(max_length=20, blank=True, null=True)
    offer_by = models.CharField(max_length=50, blank=True, null=True)
    enrolled = models.CharField(max_length=10, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    skill_gain = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=15, blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    course_image = models.CharField(max_length=4096, blank=True, null=True)
    domain_topic = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    
class Review(models.Model):
    star = models.IntegerField(blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)
    reviewer = models.CharField(max_length=50, blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)
    review_vote = models.IntegerField(blank=True, null=True)
    review_link = models.CharField(max_length=200, blank=True, null=True)
    course_tag = models.ForeignKey(CourseHeader, related_name='review', on_delete=models.CASCADE, db_column='course_tag', blank=True, null=True)

class User(models.Model):
    #id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    userid = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True, unique=True)
    avatar = models.CharField(max_length=4096, blank=True, null=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=4000, blank=True, null=True)
    role = models.IntegerField(default=1)
    isactive = models.IntegerField(db_column='isActive', default=1)  # Field name made lowercase.
    provider = models.CharField(max_length=20, default="local")
    type1 = models.CharField(max_length=50, blank=True, null=True)
    type2 = models.CharField(max_length=50, blank=True, null=True)
    type3 = models.CharField(max_length=50, blank=True, null=True)
    time_onscreen_page = models.ForeignKey(CourseHeader,related_name='time_onscreen_page',on_delete= models.DO_NOTHING, db_column='time_onscreen_page', blank=True, null=True)
    most_action_each_page = models.ForeignKey(CourseHeader,related_name='most_action_each_page',on_delete= models.DO_NOTHING, db_column='most_action_each_page', blank=True, null=True)
    most_url_click = models.ForeignKey(CourseHeader,related_name='most_url_click',on_delete= models.DO_NOTHING, db_column='most_url_click', blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True, default=timezone.now)