from django import forms
from .models import Pdf

class AddProduct(forms.ModelForm):
    title = forms.CharField(max_length=255)
    product_type = forms.ChoiceField(choices=Pdf.PRODUCT_TYPES)

    class Meta:
        model = Pdf
        fields = ['title', 'product_type','pdf_file']


    def save(self, commit=True, user=None):
        # Save the form data to the database
        instance = super().save(commit=False)
        if user:
            instance.author = user
        if commit:
            instance.save()