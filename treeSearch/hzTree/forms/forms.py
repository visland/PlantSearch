from django import forms
from django.forms import ModelForm, Select, TextInput, CheckboxSelectMultiple

BLOOM_COLOR_CONDITION_CHOICES = (
    ('红色', '红色'),
    ('黄色', '黄色'),
    ('紫色', '紫色'),
)

FRUIT_COLOR_CONDITION_CHOICES = (
    ('白色', '白色'),
    ('黄色', '黄色'),
    ('红色', '红色'),
)

class QueryUserForm(forms.Form):
    queryContent = forms.CharField(required=False,
                                    widget=forms.TextInput(attrs={'class': 'form-control is-invalid',
                                                                'placeholder': 'I Love you :)'}))

    bloom_color_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=BLOOM_COLOR_CONDITION_CHOICES,
    )

    fruit_color_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FRUIT_COLOR_CONDITION_CHOICES,
    )

    