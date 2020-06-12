from django import forms


# CONTACT FORM
# REQUIRED = TRUE by DEFAULT
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
