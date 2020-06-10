from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    subject = forms.ChoiceField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
