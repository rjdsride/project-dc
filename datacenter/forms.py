from django.core.exceptions import ValidationError
from django import forms

from datacenter.models import Cable

class CableForm(forms.ModelForm):
    ponta_a = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Example : XGI 0/0/0'
            }
        ),
        help_text='Por Favor não macaquear o programa'
    )
    ponta_b = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Example : XGI 0/0/0'
            }
        ),
        help_text='Escolha sabiamente entre : XGI ETH, Gb ETH,TENGb ETH,100Gb ETH,ETH TRUNK'
    )
    class Meta:
        model = Cable
        fields = (
            'nep',
            'dev_a',
            'ponta_a',
            'dev_b',
            'ponta_b',
            'description',
            'group_dev',
        )
    
    #def clean(self):
# self.
    #return super().clean()
    
    
    def clean_nep(self):
        nep = self.cleaned_data.get('nep')
        if self.instance and self.instance.pk:  # Verifica se o formulário está atualizando um cabo existente
            original_nep = Cable.objects.get(pk=self.instance.pk).nep
            if original_nep != nep:  # Se o NEP foi alterado
                if Cable.objects.filter(nep=nep).exists():
                    raise ValidationError("Já existe um cabo com este NEP.")
        else:  # Se o formulário está criando um novo cabo
            if Cable.objects.filter(nep=nep).exists():
                raise ValidationError("Já existe um cabo com este NEP.")
        return nep
    
    def clean(self):
        cleaned_data = super().clean()
        dev_a = cleaned_data.get('dev_a')
        dev_b = cleaned_data.get('dev_b')

        if not dev_a and not dev_b:
            raise ValidationError("Ambos os campos dev_a e dev_b não podem ser nulos.")
        elif dev_a and dev_b and dev_a == dev_b:
            raise ValidationError("Ta macaqueando rapaz? Onde já se viu colocar duas pontas do mesmo cabo no mesmo dispositivo?")

        return cleaned_data