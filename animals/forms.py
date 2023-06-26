
from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'date_of_birth']

class UploadFileForm(forms.ModelForm):
    file = forms.FileField()


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'video_file', 'tags')



