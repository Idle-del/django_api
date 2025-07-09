import django_filters
from .models import Employee
from django.db.models.functions import Lower

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    # emp_id = django_filters.RangeFilter(field_name='emp_id')
    min_id = django_filters.CharFilter(method='filter_by_range_id', label = 'From Employee ID', lookup_expr='iexact')
    max_id = django_filters.CharFilter(method='filter_by_range_id', label = 'To Employee ID', lookup_expr='iexact')

    class Meta:
        model = Employee
        fields = ['designation', 'emp_name', 'min_id', 'max_id']

    def filter_by_range_id(self, queryset, name, value):
        if value:
            queryset = queryset.annotate(lower_emp_id=Lower('emp_id'))
            if name == 'min_id':
                return queryset.filter(lower_emp_id__gte=value)
            elif name == 'max_id':
                return queryset.filter(lower_emp_id__lte=value)
            return queryset