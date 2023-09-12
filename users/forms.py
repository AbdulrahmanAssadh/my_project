
# from django import forms


# class FormLoginUser(forms.Form):
#     name= forms.CharField(label='Your name', max_length=100)
#     email= forms.CharField(label='Your email', max_length=100)
#     password=forms.CharField(label='Your password',max_length=10)


from django.forms  import ModelForm

from users.models import Student



class  FormLoginUser(ModelForm):
    class Meta:
        model = Student
        fields = ['name','age','email']
        