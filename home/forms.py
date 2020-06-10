from django import forms


# CONTACT FORM
# REQUIRED = TRUE by DEFAULT
class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length='100')
    email = forms.EmailField(label='Your email', max_length='100')
    message = forms.CharField(widget=forms.Textarea)
