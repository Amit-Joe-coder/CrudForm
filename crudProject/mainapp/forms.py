from django import forms
from mainapp.models import student_model

class student_form(forms.ModelForm):
    #name=forms.CharField(max_length=50)
    #roll=forms.IntegerField()
    #marks=forms.IntegerField()
    class Meta:
        model=student_model
        fields='__all__'
    
    

