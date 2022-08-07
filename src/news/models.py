from django.db import models

class News(models.Model):
    class Stock(models.TextChoices):
        TSLA = "TSLA", "TSLA"
        FB = "FB", "FB"
        AMZN = "AMZN", "AMZN"
        TWTR = "TWTR", "TWTR"
        NFLX = "NFLX", "NFLX"
    
    stock = models.CharField(
        verbose_name="stock",
        blank=True,
        default="",
        max_length=32,
        choices=Stock.choices,
    )
    category = models.CharField(
        verbose_name="category",
        blank=True,
        default="",
        max_length=256,
    )
    datetime = models.DateTimeField(
        verbose_name="datetime",
        null=True,
        blank=True,
    )
    headline = models.CharField(
        verbose_name="headline",
        blank=True,
        default="",
        max_length=256,
    )
    news_id = models.IntegerField(
        verbose_name="news_id",
        unique=True,
    )
    image = models.URLField(
        verbose_name="image",
        blank=True,
        default="",
        max_length=512,
    )
    related = models.CharField(
        verbose_name="related",
        blank=True,
        default="",
        max_length=128,
    )
    source = models.CharField(
        verbose_name="source",
        blank=True,
        default="",
        max_length=128,
    )
    summary = models.TextField(
        verbose_name="summary",
        blank=True,
        default="",
        max_length=1024,
    )
    url = models.URLField(
        verbose_name="url",
        blank=True,
        default="",
    )

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        db_table = "news.news"
