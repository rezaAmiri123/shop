#!/bin/sh

# wait for PSQL server to start
# sleep 10

cd project
celery worker -A config -l info
