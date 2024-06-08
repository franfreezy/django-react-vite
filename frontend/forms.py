from django import forms
from .models import user

class PostForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name','last_name','email','reg_date']
        exclude = ['reg_date']