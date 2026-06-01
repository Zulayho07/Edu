from django.urls import path

from .views import home, student_by_course, student_detail

urlpatterns = [
    path('', home, name='home'),
    path('courses/<int:course_id>', student_by_course, name='student_by_course'),
    path('student/<int:student_id>/', student_detail, name='detail'),
]
