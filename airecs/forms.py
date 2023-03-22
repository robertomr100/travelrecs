from django import forms

class TripForm(forms.Form):
    location = forms.CharField(
        label='Enter where you are going',
        widget=forms.TextInput(attrs={'required': True}),
    )
    interests = forms.CharField(
        label='Enter interests (comma-separated):',
        widget=forms.TextInput(attrs={'required': True}),
    )
    number_of_days = forms.IntegerField( label='Enter number of days:',
        widget=forms.NumberInput(attrs={'required': True}),)