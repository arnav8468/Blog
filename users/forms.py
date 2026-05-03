from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'bio')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded border'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 rounded border'}),
            'bio': forms.Textarea(attrs={'class': 'w-full px-4 py-2 rounded border', 'rows': 3}),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'bio', 'website')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded border'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 rounded border'}),
            'bio': forms.Textarea(attrs={'class': 'w-full px-4 py-2 rounded border', 'rows': 3}),
            'website': forms.URLInput(attrs={'class': 'w-full px-4 py-2 rounded border'}),
        }
