from django import forms
from . models import User
from django.utils.translation import ugettext_lazy as _


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'email', 'message']
#         widgets = {
#             'name': forms.TextInput(attrs={'title': 'Name',
#                                            'class': 'form-control', 'placeholder': 'Enter your name'}),

#             'email': forms.TextInput(attrs={
#                 'class': 'form-control', 'placeholder': 'Enter email'}),

#             'message': forms.Textarea(attrs={
#                 'class': 'form-control', 'placeholder': 'Type in your messages'}),
#         }


class UserForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=150, widget=forms.TextInput(attrs=
                                        {
                                            'class': 'form-control',
                                            'placeholder': 'Name'
                                        }))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs=
                                        {
                                            'class': 'form-control',
                                            'placeholder': 'Enter email'
                                        }))
    message = forms.CharField(widget=forms.Textarea(attrs=
                                        {
                                            'class': 'form-control',
                                            'placeholder': 'Type in your messages'
                                        }))
    
    class Meta:
        model = User
        fields = ['name', 'email', 'message']
