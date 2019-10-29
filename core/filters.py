import django_filters
from .models import libro

class filtrolibros(django_filters.FilterSet):

    class Meta:
        model = libro 
        fields = {
            'titulo':['icontains'],
        }
