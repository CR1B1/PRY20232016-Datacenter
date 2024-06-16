import django_filters
import authentication.models as models
from django.db.models import CharField, ForeignKey
from django import forms 

ROLES_CHOICES = ((512,'Administrator'),(255, 'Manager'), (1, 'Empleado'))

class UserFilter(django_filters.FilterSet):
    user_area = django_filters.ModelChoiceFilter(queryset=models.UserArea.objects.all(),field_name='user_area',widget=forms.Select(attrs={'class': 'form-control'}))
    administrator = django_filters.ModelChoiceFilter(queryset=models.User.objects.filter(role=512),field_name='administrator',widget=forms.Select(attrs={'class': 'form-control'}))
    role = django_filters.ChoiceFilter(label="Rol",field_name="role", lookup_expr="icontains", choices=ROLES_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Prioridad'}))
    class Meta:
        model = models.User
        fields = ['user_area', 'administrator', 'role']