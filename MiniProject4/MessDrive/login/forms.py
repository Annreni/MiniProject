from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Inmate, Staff, User 
from django import forms

class InmateSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    phone_number = forms.CharField(required = True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit = False)
        user.is_inmate = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        inmate = Inmate.objects.create(user = user)
        inmate.phone_number = self.cleaned_data.get('phone_number')
        inmate.save();
        return user

            

class StaffSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    phone_number = forms.CharField(required = True)
    role = forms.CharField(required = True)

    class Meta(UserCreationForm.Meta):
        model = User        
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit = False)
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        staff = Staff.objects.create(user = user)
        staff.phone_number = self.cleaned_data.get('phone_number')
        staff.role = self.cleaned_data.get('role')
        staff.save();
        return user
    
