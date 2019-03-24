from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea,required=False)
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
        )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': ' Enter your First name  Ex : Tom'}),label="")
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': ' Enter your Last name  Ex : Cruise'}),label="")
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'placeholder': ' Enter your Email Ex : jidnyesh@gmail.com'}),label="")
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': ' Enter your username  Ex : tom123'}),label="")
    password1 = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': ' Enter your new password'}),label="")
    password2 = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': ' Enter your password again'}),label="")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2','first_name','last_name','email']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        )


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
        )
        exclude = (
            'password',
            'password2'
        )