from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone_number',)


class CustomUserChangeForm(UserChangeForm, forms.ModelForm):
    add_bonus = forms.IntegerField(label='Добавить бонусы', required=False)
    subtract_bonus = forms.IntegerField(label='Отнять бонусы', required=False)

    def clean(self):
        cleaned_data = super().clean()
        add_bonus = cleaned_data.get('add_bonus')
        subtract_bonus = cleaned_data.get('subtract_bonus')
        if add_bonus and subtract_bonus:
            raise forms.ValidationError('Нельзя одновременно добавить и отнять бонусы')
        return cleaned_data

    class Meta:
        model = User
        fields = ('phone_number',)
