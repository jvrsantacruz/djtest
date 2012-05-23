from django import forms
from django.forms import ModelForm

from djtest.models import PressNew


class SendPressNewForm(ModelForm):
    "New upload formulary. Binded to PressNew"
    img = forms.FileField(required=False, help_text="Optional attached image")

    class Meta:
        model = PressNew
        fields = ('title', 'media', 'url', 'img', 'comment')
