#!/bin/bash
connect_to_service() {
    while !</dev/tcp/$1/$2
    do sleep 1
    done
}
export_envs() {
    set -a
    . /src/core/.env
    set +a
}
export_envs
case "$PROCESS" in
"DJANGO_DEV")
    connect_to_service "${DB_HOST}" "${DB_PORT}"
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
    ;;
"CELERY_DEV")
    connect_to_service "${DB_HOST}" "${DB_PORT}"
    connect_to_service "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A core worker --loglevel=INFO \
    -B --concurrency=1
    ;;
*)
    echo "Wrong PROCESS"
    exit 1
    ;;
esac