# Zimran Test Task

To start this project run

```
docker-compose up
```

## Part 1

`get_news` celery task in `news` app runs every hour, fetches news about required stocks on that day and saves them to database


## Part 2

Endpoint for fetching list of news: `http://0.0.0.0:8000/api/news/`

Query Parameters for Filtering:
- `stock`
- `date_from`
- `date_to`

Example request:
```
curl --location --request GET 'http://0.0.0.0:8000/api/news/?stock=TSLA&date_from=2022-08-01&date_to=2022-08-01'
```

## Note**

Since task is run only once an hour and only for current day, there might be only few or even zero news returned from Finhub on initial tests

To solve this problem I have developed additional logic for running task on particular dates

There is an endpoint `http://0.0.0.0:8000/api/news/news_in_range/` which will receive `POST` request with information on dates

Example body:
```
{
    "from_date": "2022-07-01",
    "to_date": "2022-07-01"
}
```

It will then run task in background for fetching news on these particular dates

Example request:
```
curl --location --request POST 'http://0.0.0.0:8000/api/news/news_in_range/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "from_date": "2022-07-01",
    "to_date": "2022-07-01"
}'
```
