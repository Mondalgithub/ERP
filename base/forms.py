from django import forms
from django.forms import ModelForm
from .models import CustomUser, LeaveRequest
from django.contrib.auth.forms import UserCreationForm

class Update(ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'USN', 'course', 'gender', 'room_no', 'block_name', 'sharing', 'mother_name', 'father_name', 'contact', 'mother_contact', 'father_contact')


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['name', 'reason', 'contact_details', 'location']