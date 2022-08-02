from django import forms

from .models import CardData

class AddPasswordForm(forms.Form):
    CAT_CHOICES = [
        ('OS', 'Online Sites'),
        ('Lp', 'Laptop'),
        ('PC', 'Pc'),
        ('MB', 'Mobile'),
        ('W', 'Wallets'),
        ('OTHER', 'Other')
    ]
    title = forms.CharField(label='Title/Site Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=CAT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}))

class CcDataForm(forms.ModelForm):
    cc_number = forms.CharField(label='Card Number', max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cc_holder_name = forms.CharField(label='Card Holder Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exp_date = forms.CharField(label='Expiry Date', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ccv_code = forms.CharField(label='CCV/Security Code', max_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cc_notes = forms.CharField(label="Notes", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}))
    class Meta:
        model = CardData
        fields = ['cc_number', 'cc_holder_name', 'exp_date', 'ccv_code', 'cc_notes',]
