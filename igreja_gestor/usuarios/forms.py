from django import forms
from django.contrib.auth.models import User

class CadastroUsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'senha', 'confirmar_senha']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")

class LoginUsuarioForm(forms.Form):
    username = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)