from django.forms import ModelForm
from .models import Transacao
from .models import Document

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['description', 'document']