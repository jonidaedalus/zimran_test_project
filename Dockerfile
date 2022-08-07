FROM python:3.9.6-slim

ENV PYTHONUNBUFFERED=1

ADD ./src/requirements.txt /src/

RUN pip install -r /src/requirements.txt

COPY ./src /src

WORKDIR /src

CMD ["./entrypoint.sh"]
