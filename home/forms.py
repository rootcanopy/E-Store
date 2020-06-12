from django import forms
from crispy_forms.helper import FormHelper


# CONTACT FORM
# REQUIRED = TRUE by DEFAULT
class ContactForm(forms.Form):
    name = forms.CharField()
    email_from = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
