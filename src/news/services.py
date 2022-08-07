import logging

from django.conf import settings
from django.db import IntegrityError
from django.utils.timezone import datetime
import requests

from .models import News
from .serializers import NewsCreateSerializer


class FinhubService:
    company_news_url = "https://finnhub.io/api/v1/company-news"
    headers = {
        "X-Finnhub-Token": settings.X_FINHUB_TOKEN,
    }

    def __init__(self) -> None:
        today = datetime.today().date()
        self.from_date = str(today)
        self.to_date = str(today)

    @staticmethod
    def create_news(news_list: list, stock: str) -> None:
        for news_data in news_list:
            news_data.update({"stock": stock})
            serializer = NewsCreateSerializer(data=news_data)
            serializer.is_valid(raise_exception=True)
            try:
                serializer.save()
            except IntegrityError:
                logging.warning("Duplicate news")
    
    def send_request(self, url: str, params: dict) -> list:
        try:
            response = requests.get(
                url=url,
                headers=self.headers,
                timeout=5,
                params=params,
            )
            response.raise_for_status()
            return response.json()
        except:
            logging.error("Error sending requrest to finhub")
            return []

    def get_min_id(self, stock: str) -> int:
        last_news = News.objects.filter(stock=stock).order_by("-news_id").first()
        if not last_news:
            return 0
        return last_news.news_id

    def get_news_for_stock(self, stock: str) -> None:
        min_id = self.get_min_id(stock)
        params = {"symbol": stock, "from": self.from_date, "to": self.to_date, "minId": min_id}
        news_list = self.send_request(self.company_news_url, params)
        self.create_news(news_list, stock)

    def get_news(self) -> None:
        for stock, _ in News.Stock.choices:
            self.get_news_for_stock(stock) 


class CustomDatesFinhubService(FinhubService):
    def __init__(self, from_date: str, to_date: str):
        self.from_date = from_date
        self.to_date = to_date
