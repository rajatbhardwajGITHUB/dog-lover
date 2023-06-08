from django import forms
from .models import Users_info, Dog, Users

class basic_info_form(forms.Form):


    name = forms.CharField(label = 'Name',max_length=50, required=True)
    email = forms.EmailField(label='Email', required=True)
    dogname = forms.CharField( max_length=50,required=True)
    dogbreed = forms.CharField(max_length=50, required=True)

    class meta:
        userModel = Users_info
        fields = ['Uname', 'Uemail']
        dogModel = Dog
        fields = ['dogName','dogBreed']

class loginForm(forms.Form):

    username = forms.CharField(label='username', max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)

    

class signUp(forms.Form):
    name = forms.CharField(label="Name",max_length=50, required=True)
    email = forms.EmailField(label="Email", max_length=50, required=True)
    password = forms.CharField(label="Password", max_length=50, required=True)

    class meta:
        users = Users
        fields = ["uName","uEmail","uPass"]

