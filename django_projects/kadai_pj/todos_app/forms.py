from django import forms

class TodoSearchForm(forms.Form):
    user_id = forms.IntegerField(
        label='ユーザーID', 
        min_value=1, 
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ユーザーIDを入力'})
    )