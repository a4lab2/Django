from django.urls import path

from . import views

urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherList.as_view()),
    path('teacher-login', views.teacher_login),



    path('category/', views.CategoryList.as_view()),

    path('course/', views.CourseList.as_view()),
    path('chapter/', views.ChapterList.as_view()),
    path('teacher-course/<int:teacher_id>', views.TeacherCourseList.as_view()),
]