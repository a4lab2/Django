from django.urls import path

from . import views

urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login', views.teacher_login),
    path('category/', views.CategoryList.as_view()),
    path('course/', views.CourseList.as_view()),
    path('chapter/<int:pk>', views.ChapterDetailView.as_view()),
    path('course/<int:pk>', views.CourseDetailView.as_view()),
    path('course-chapters/<int:course_id>', views.CourseChapterList.as_view()),
    path('teacher-courses/<int:teacher_id>', views.TeacherCourseList.as_view()),
    path('teacher-course-detail/<int:pk>', views.TeacherCourseDetail.as_view()),

]