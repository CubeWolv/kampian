from django import forms
from django.contrib.auth.models import User  # Make sure to import the User model
from .models import Updates  # Correct the model import

class AddUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=500, required=False)  # Make description optional
    img = forms.FileField()

    class Meta:
        model = Updates  # Use the correct model name
        fields = ['title', 'description', 'img']

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.author = user
        if commit:
            instance.save()
        return instance
