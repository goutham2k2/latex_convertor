from django import forms

class TextInputForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 10,
        'cols': 80,
        'placeholder': 'Paste your text with equations here...'
    }))
