from django import forms

class HousePriceForm(forms.Form):
    bhk_no = forms.IntegerField(label="Bedrooms (BHK)")
    square_ft = forms.FloatField(label="Total Square Feet")
