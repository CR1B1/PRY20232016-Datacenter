from django import forms
from authentication.models import UserArea
import public.models as models

class IncidenceForm(forms.ModelForm):
    incidence_detail = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Detalle de la incidencia",
                "rows":"12"
            }
        ), label="")
    class Meta:
        model = models.Incidence
        fields = ['incidence_detail']
        
class AccessRequestForm(forms.Form):
    class Meta:
        model = models.AccessRequest
        fields = '__all__'
        
class SubjectForm(forms.Form):
    subject_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "form-control"
            }
        ))
    
    priority = forms.ChoiceField(
        choices=[(2,'High'),(1, 'Medium'), (0, 'Low')],
        widget = forms.Select(attrs={
                "placeholder": "Prioridad",
                "class": "form-select form-select-sm mb-3 input-box",
            }, choices=[(2,'High'),(1, 'Medium'), (0, 'Low')]),
    )
        
class UserAreaForm(forms.Form):
    class Meta:
        model = UserArea
        fields = '__all__'
        
class UserPermissionForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['authorization']
        
class UserChangePasswordForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Correo electronico",
                "class": "form-control"
            }
        ))
    class Meta:
        model = models.User
        fields = ['email']
        
class LogoForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['company_logo']
