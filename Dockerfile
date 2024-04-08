ARG PYTHON_VERSION=3.12-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code


# collect static files 
# RUN python manage.py collectstatic --noinput
RUN --mount=type=secret,id=DATABASE_URL \
  DATABASE_URL="$(cat /run/secrets/DATABASE_URL)" \
  python manage.py collectstatic --noinput


EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "kjon_django.wsgi"]
