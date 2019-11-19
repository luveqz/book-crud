FROM python:3.8.0-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update
# django-simple-captcha dependencies.
RUN apt-get install -y libz-dev libjpeg-dev libfreetype6-dev python-dev

RUN addgroup --system django \
    && adduser --system --ingroup django django

COPY ./api/requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /requirements

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./compose/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
RUN chown django /start
COPY ./api /app

RUN chown -R django /app

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
