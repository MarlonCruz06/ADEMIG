from django import forms
from .models import Inscricao

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['evento', 'membro', 'pagamento', 'data_inscricao']
        widgets = {
            'data_inscricao': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'evento': 'Evento',
            'membro': 'Membro',
            'pagamento': 'Pagamento',
            'data_inscricao': 'Data da Inscrição',
        }