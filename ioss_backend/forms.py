from django import forms

class URLForm(forms.Form):
    original_url = forms.URLField(label='Enter URL', max_length=2048, widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}))
