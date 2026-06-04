from django.shortcuts import render, redirect

from .forms import CourseForm, StudentForm
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


def add_course(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CourseForm(request.POST)
            if form.is_valid():
                course = form.save()
                return redirect('student_by_course', course_id=course.pk)
        else:
            form = CourseForm()
        context = {
            'form': form,
        }
        return render(request, 'courses/add_course.html', context)
    else:
        return redirect('home')


def update_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('student_by_course', course_id=course.pk)
    else:
        form = CourseForm(instance=course)
    context = {
        'form': form,
    }
    return render(request, 'courses/add_course.html', context)




def add_student(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                student = form.save()
                return redirect('detail', student_id=student.pk)
        else:
            form = StudentForm()
        context = {
            'form': form,
        }
        return render(request, 'courses/add_student.html', context)
    else:
        return redirect('home')


def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('detail', student_id=student.pk)
    else:
        form = StudentForm(instance=student)
    context = {
        'form': form,
    }
    return render(request, 'courses/add_student.html', context)
