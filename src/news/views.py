from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import NewsFilter
from .models import News
from .serializers import NewsReadSerializer, CreateNewsInRangeSerializer
from .tasks import get_news_in_range


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsReadSerializer
    http_method_names = ("get", "post")
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NewsFilter

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed(method="GET")
    
    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(method="GET")

    @action(detail=False, methods=["post"])
    def news_in_range(self, request, *args, **kwargs):
        self.serializer_class = CreateNewsInRangeSerializer
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        get_news_in_range.apply_async(kwargs=request.data)
        return Response(status=status.HTTP_200_OK)
