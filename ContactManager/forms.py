from django import forms
from django.core.validators import EmailValidator, URLValidator
from django.forms import ModelForm
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'serial_number',
            'full_name',
            'company',
            'branch',
            'department',
            'title',
            'ext_number',
            'phone',
            'phone1',
            'phone2',
            'email',
            'website_link',
            'whatsapp_link',
            'facebook_link',
            'twitter_link',
            'tiktok_link',
            'instagram_link',
            'zoom_link',
            'teams_link',
            'telegram_link',
            'gmail_link',
            'outlook_link',
            'linkedIn_link',
            'Messaanger_link',
            'address',

        ]
