FROM python:3.9.13-alpine3.16

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /home/

RUN echo "Installing apk packages..." \
    && apk update \
    && apk --no-cache add \
    gcc \
    curl \
    libc-dev \
    musl-dev \
    libffi-dev \
    python3-dev \
    postgresql-dev

COPY ./requirements.txt ./

RUN echo "Installing pip packages..." \
    && pip install -U pip \
    && pip install --no-cache-dir -r ./requirements.txt \
    && rm ./requirements.txt

COPY ./my_os/ ./my_os/

WORKDIR /home/my_os/
