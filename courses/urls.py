from django.urls import path

from .views import home, student_by_course, student_detail, add_student, update_student, add_course, update_course

urlpatterns = [
    path('', home, name='home'),
    path('courses/<int:course_id>', student_by_course, name='student_by_course'),
    path('courses/<int:course_id>/update/', update_course, name='update_course'),
    path('courses/add/', add_course, name='add_course'),
    path('student/<int:student_id>/', student_detail, name='detail'),
    path('student/<int:student_id>/update/', update_student, name='update_student'),
    path('student/add/', add_student, name='add_student'),
]
