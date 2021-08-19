from django import forms
from .models import Order
from django.forms.widgets import DateInput, TimeInput

import datetime


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2', 'town_or_city',
                  'postcode', 'optional_notes', 'pickup_date', 'pickup_time')
        widgets = {
            'pickup_date': DateInput(
                attrs={'min': datetime.date.today, 'type': 'date'}),
            'pickup_time': TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'optional_notes': 'Optional Notes',
            'pickup_date': 'Pickup Date',
            'pickup_time': 'Pickup Time',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
