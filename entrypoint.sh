#!/bin/bash

celery -A celery_worker.celery worker --loglevel=INFO --pool=solo &

exec "$@"
