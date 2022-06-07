FROM alpine:3.16.0

WORKDIR /home/

RUN echo "Installing apk packages..." \
    && apk update \
    && apk --no-cache add py3-pip

COPY ./requirements.txt ./

RUN echo "Installing pip packages..." \
    && pip install -U pip \
    && pip install --no-cache-dir -r ./requirements.txt \
    && rm ./requirements.txt

COPY ./src/wsgi.py ./

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:application"]
