from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Store
from .models import Sale

class LoginForm(AuthenticationForm):
    pass


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name','location']
        
        
    def save(self,user,commit=True):
        instance=super().save(commit=False)
        if user:
            instance.owner=user
            instance.save()
        return instance
        

class SaleForm(forms.ModelForm):
    class Meta:
        model=Sale
        fields='__all__'