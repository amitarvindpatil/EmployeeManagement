from django import forms


class ImageUploadForm(forms.Form):
    """Image upload form."""
    photo = forms.FileField()
