from django import forms

from uploads.core.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class TextForm(forms.Form)
    searched=forms.CharField(label="searched",max max_length=1000)


