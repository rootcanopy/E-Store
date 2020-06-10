from django import forms


# CONTACT FORM
# REQUIRED = TRUE by DEFAULT
class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your message'
            }
        )
    )

