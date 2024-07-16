# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import transaction
from .models import User, Patient, Doctor,Blog

class PatientSignUpForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(required=True, label='password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, label='confirm password(again)',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    line1 = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pincode = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'upload a profile picture'}))
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()

        patient = Patient.objects.create(user=user)
        patient.profile = self.cleaned_data.get('profile')
        patient.line1 = self.cleaned_data.get('line1')
        patient.state = self.cleaned_data.get('state')
        patient.pincode = self.cleaned_data.get('pincode')
        patient.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(required=True, label='password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, label='confirm password(again)',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    line1 = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pincode = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'upload a profile picture'}))
    experience = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()

        doctor = Doctor.objects.create(user=user)
        doctor.profile = self.cleaned_data.get('profile')
        doctor.line1 = self.cleaned_data.get('line1')
        doctor.state = self.cleaned_data.get('state')
        doctor.pincode = self.cleaned_data.get('pincode')
        doctor.experience = self.cleaned_data.get('experience')
        doctor.save()
        return user


# blog form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','image', 'category', 'content', 'summary']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'title of the post'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'title of the image'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select category'}),
            'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'title content '}),
            'summary':forms.Textarea(attrs={'class':'form-control', 'placeholder':'summary '}),
        }