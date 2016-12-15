from django import forms


class ImageForm(forms.Form):
    image = forms.FileField(
        label='Select a file'
    )