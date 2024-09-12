from django import forms
from VPEApp.models import EvaluationType, UsersList

class EvalForms(forms.ModelForm):
    class Meta:
        model = EvaluationType
        fields = '__all__'

class UsersForms(forms.ModelForm):
    class Meta:
        model = UsersList
        fields = '__all__'