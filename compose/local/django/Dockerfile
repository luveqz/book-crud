FROM python:3.8.0-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update
# https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
RUN apt-get install -y postgresql-client \
    # django-simple-captcha dependencies.
    && apt-get install -y libz-dev libjpeg-dev libfreetype6-dev python-dev

COPY ./api/requirements /requirements
RUN pip3 install  -r /requirements/local.txt

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
