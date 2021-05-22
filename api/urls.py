from django.urls import path
from .views import  CreateUser, SocialLoginView, UserView, LocalLoginView, CourseView, CreateCourse, RelatedCourse,CourseSearchView,Login

urlpatterns = [
    path('create-user', CreateUser.as_view()),
    path('oauth/login/', SocialLoginView.as_view()),
    path('user', UserView.as_view()),
    path('get-user',LocalLoginView.as_view()),
    path('course',CourseView.as_view()),
    path('create-course',CreateCourse.as_view()),
    path('relatedcourse',RelatedCourse.as_view()),
    path('course-list', CourseSearchView.as_view()),
    path('auth/login/',Login.as_view())
]