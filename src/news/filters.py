from django_filters import rest_framework as filters

from .models import News


class NewsFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name="datetime", lookup_expr="date__gte")
    date_to = filters.DateFilter(field_name="datetime", lookup_expr="date__lte")

    class Meta:
        model = News
        fields = ("stock", "date_from", "date_to")