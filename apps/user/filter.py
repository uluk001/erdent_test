from django_filters import rest_framework as qwerty

from apps.user.models import User



def get_client_ip(request):
    """Получение IP пользоваеля"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class CharFilterInFilter(qwerty.BaseInFilter, qwerty.CharFilter):
    pass

class DoctorFilter(qwerty.FilterSet):
    branch = CharFilterInFilter(field_name='branch', lookup_expr='in')
    class Meta:
        model = User 
        fields = ['branch']
