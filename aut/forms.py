from django import forms

from captcha.fields import ReCaptchaField


class ForgetPasswordForm(forms.Form):
    """
    форма валидации для Recaptcha v2
    """

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
    )

    captcha = ReCaptchaField()
