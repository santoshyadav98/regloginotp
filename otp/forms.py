from django import forms
from otp.models import Reg
class RegForm(forms.ModelForm):
    class  Meta:
        model=Reg
        fields='__all__'
        
