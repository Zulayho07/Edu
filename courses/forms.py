from django import forms
from .models import Course, Student
from django.core.exceptions import ValidationError



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Nomi',
                'class': 'form-control',

            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'Tasnifi',
                'class': 'form-control',
            }),
            'duration': forms.NumberInput(attrs={
                'placeholder': 'Davomiyligi',
                'class': 'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Narxi',
                'class': 'form-control',
            })
        }
        labels = {
            'title': 'Nomi',
            'description': 'Tasnifi',
            'duration': 'Davomiyligi',
            'price': 'Narxi',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and len(title) > 100:
            raise ValidationError('Nomi 100 ta simvoldan uzun bo\'lmasligi kerak')
        return title

    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if duration and duration > 15 or duration <= 0:
            raise ValidationError('Kurs davomiyligi 15 oydan oshmagan musbat qiymat bolsin!')
        return duration

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price <=0:
            raise ValidationError('Musbat qiymat kiriting')
        return price

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Ismi',
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Familyasi',
                'class': 'form-control',
            }),
            'birth_year': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Tug\'ilgan yili',
                'class': 'form-control',
            }),
            'phone_number': forms.NumberInput(attrs={
                'type': 'tel',
                'placeholder': 'Telefon raqami',
                'class': 'form-control',
            }),
            'course': forms.Select(attrs={
                'placeholder': 'Kursi',
                'class': 'form-control',
            })
        }
        labels = {
            'first_name': 'Ismi',
            'last_name': 'Familyasi',
            'birth_year': 'Tug\'ilgan yili',
            'phone_number': 'Telefon raqami',
            'course': 'Kursi',
        }


        