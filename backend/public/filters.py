import django_filters
import public.models as models
from authentication.models import UserArea
from django_filters.widgets import RangeWidget
from django import forms

PRIORITY_CHOICES = (
    ("MEDIA", "Media"),
    ("BAJA", "Baja"),
    ("ALTA", "Alta"),
    ("CRITICA", "Critica"),
)

SOLVED_CHOICES = ((True, 'Solucionado'), (False, 'No solucionado'), (None, 'Todos'))

class IncidenceFilter(django_filters.FilterSet):
    incidence_subject = django_filters.ChoiceFilter(label="Prioridad",field_name="incidence_subject__priority", lookup_expr="icontains", choices=PRIORITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Prioridad'}))
    
    start_date = django_filters.DateFilter(
        field_name='create_date', lookup_expr=('gt'), label='Fecha de creacion',
        widget=forms.DateInput(
            attrs={"placeholder":"Select date", "type":"date", "id":"example", "class":"form-control"}
        )
    )
    
    final_date = django_filters.DateFilter(
        field_name ='create_date', lookup_expr=('lt'), label='Fecha de final',
        widget = forms.DateInput(
            attrs={"placeholder":"Select date", "type":"date", "id":"example", "class":"form-control"}
        )
    )
    
    solved = django_filters.BooleanFilter(
        field_name = 'solved',
        widget = forms.RadioSelect(attrs={"class":"form-check-inline"}, choices=SOLVED_CHOICES)
    )

    class Meta:
        model = models.Incidence
        fields = ['start_date', 'final_date']
        
        
class DashboardFilter(django_filters.FilterSet):
    user_area = django_filters.ModelMultipleChoiceFilter(queryset=UserArea.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), label="Areas")
    
    class Meta:
        model = models.Incidence
        fields = ['user__user_area']
