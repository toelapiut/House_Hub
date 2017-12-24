from django import forms
from .models import *
from django.db.models.fields.files import ImageFieldFile, FileField



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'post']


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=('user',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','phone','picture','username')


class HouseForm(forms.ModelForm):
    class Meta:
        model=House
        exclude=('user',)
        # fields=()

class RoomForm(forms.ModelForm):

    class Meta:
        model=Room
        exclude=('house',)