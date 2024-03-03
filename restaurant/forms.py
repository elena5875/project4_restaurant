# restaurant/forms.py

from django import forms
from datetime import time


class ReservationForm(forms.Form):
    date = forms.DateField(label='Date')
    time = forms.TimeField(label='Time', widget=forms.Select(choices=[(time(hour=h), '{:02d}:00'.format(h)) for h in range(17, 22)]))
    num_people = forms.IntegerField(label='Number of People')

    def clean_num_people(self):
        num_people = self.cleaned_data['num_people']
        if num_people > 9:
            raise forms.ValidationError("For groups larger than 9 people, please call us to make a reservation.")
        return num_people

        
