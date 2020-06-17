from django import forms

from memberships.models import Family


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ('name', 'church')
