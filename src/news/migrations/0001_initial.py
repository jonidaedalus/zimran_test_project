# Generated by Django 4.0.6 on 2022-08-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(blank=True, choices=[('TSLA', 'TSLA'), ('FB', 'FB'), ('AMZN', 'AMZN'), ('TWTR', 'TWTR'), ('NFLX', 'NFLX')], default='', max_length=32, verbose_name='stock')),
                ('category', models.CharField(blank=True, default='', max_length=256, verbose_name='category')),
                ('datetime', models.DateTimeField(blank=True, null=True, verbose_name='datetime')),
                ('headline', models.CharField(blank=True, default='', max_length=256, verbose_name='headline')),
                ('news_id', models.IntegerField(unique=True, verbose_name='news_id')),
                ('image', models.URLField(blank=True, default='', max_length=512, verbose_name='image')),
                ('related', models.CharField(blank=True, default='', max_length=128, verbose_name='related')),
                ('source', models.CharField(blank=True, default='', max_length=128, verbose_name='source')),
                ('summary', models.TextField(blank=True, default='', max_length=1024, verbose_name='summary')),
                ('url', models.URLField(blank=True, default='', verbose_name='url')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'db_table': 'news.news',
            },
        ),
    ]
