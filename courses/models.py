from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=13)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __repr__(self):
        return self.first_name + " " + self.last_name


class Comment(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

    def __repr__(self):
        return self.user
