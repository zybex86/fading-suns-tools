FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

COPY ../../requirements/requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -U pip
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /fst
WORKDIR /fst
COPY ./fst /fst

RUN adduser -D user
USER user
