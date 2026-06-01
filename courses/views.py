from django.shortcuts import render

from .models import Course, Student


def home(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    context = {
        'courses': courses,
        'students': students,
        'title': 'Courses'
    }
    return render(request, 'courses/index.html', context)


def student_detail(request, student_id):
    courses = Course.objects.all()
    student = Student.objects.get(id=student_id)
    context = {
        'courses': courses,
        'student': student,
        'title': student.last_name + ' ' + student.first_name
    }
    return render(request, 'courses/detail.html', context)


def student_by_course(request, course_id):
    courses = Course.objects.all()
    students = Student.objects.filter(course_id=course_id)
    course = Course.objects.get(id=course_id)
    context = {
        'courses': courses,
        'course': course,
        'students': students,
        'title': course.title
    }
    return render(request, 'courses/student_by_course.html', context)
